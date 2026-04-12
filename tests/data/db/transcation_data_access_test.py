from sqlalchemy.orm import sessionmaker

from luna_app.db.data_access import ContactDataAccess
from luna_app.db.entities import ContactEntity


def test_get_all_contacts(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        new_contact1: ContactEntity = ContactEntity(first_name="John", last_name="Doe")
        new_contact2: ContactEntity = ContactEntity(first_name="Jane", last_name="Doe")
        new_contact3: ContactEntity = ContactEntity(first_name="Alice", last_name="Smith")
        new_contact4: ContactEntity = ContactEntity(first_name="Bob", last_name="Brown")
        new_contact5: ContactEntity = ContactEntity(first_name="Charlie", last_name="Black")

        ContactDataAccess.save_contact(session, new_contact1)
        ContactDataAccess.save_contact(session, new_contact2)
        ContactDataAccess.save_contact(session, new_contact3)
        ContactDataAccess.save_contact(session, new_contact4)
        ContactDataAccess.save_contact(session, new_contact5)
        session.commit()

        # Retrieve all contacts
        contacts: list[ContactEntity] = ContactDataAccess.get_all_contacts(session)

        # Check if the added contact is in the list
        assert len(contacts) == 5
        assert any(c.id == new_contact1.id for c in contacts)
        assert any(c.id == new_contact2.id for c in contacts)
        assert any(c.id == new_contact3.id for c in contacts)
        assert any(c.id == new_contact4.id for c in contacts)
        assert any(c.id == new_contact5.id for c in contacts)


def test_get_contact_by_id(session_maker: sessionmaker) -> None:
    with session_maker() as session:
        # Create and save a contact
        new_contact: ContactEntity = ContactEntity(first_name="Jane", last_name="Doe")
        ContactDataAccess.save_contact(session, new_contact)
        session.commit()

        # Retrieve the contact by ID
        retrieved_contact: ContactEntity | None = ContactDataAccess.get_contact_by_id(session, new_contact.id)

        # Check if the retrieved contact matches the added contact (should be same instance due to same session)
        assert retrieved_contact is new_contact
