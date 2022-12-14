from typing import *
from flask import abort, make_response

from src.config import db
from src.models import Person, people_schema, person_schema


def create(person: Dict[str,str]) -> Tuple[Dict[str,str],int]:
    """
    Description.
    
    """
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(
            406,
            f"Person with last name {lname} already exists",
        )


def delete(lname: str) -> str:
    """
    Description.
    
    """
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )


def read_all() -> List[Dict[str,str]]:
    """
    Description.
    
    """
    people = Person.query.all()
    return people_schema.dump(people)


def read_one(lname: str) -> Dict[str,str]:
    """
    Description.
    
    """
    person = Person.query.filter(Person.lname == lname).one_or_none()
    if person is not None:
        return person_schema.dump(person)
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )


def update(lname: str, person: Dict[str,str]) -> Dict[str,str]:
    """
    Description.
    
    """
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()
    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )
