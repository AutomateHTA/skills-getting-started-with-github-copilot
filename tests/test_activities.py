import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(autouse=True)
def reset_activities():
    """Arrange: reset the in-memory activity data before each test."""
    activities.clear()
    activities.update(
        {
            "Chess Club": {
                "description": "Learn strategies and compete in chess tournaments",
                "schedule": "Fridays, 3:30 PM - 5:00 PM",
                "max_participants": 12,
                "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
            },
            "Programming Class": {
                "description": "Learn programming fundamentals and build software projects",
                "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
                "max_participants": 20,
                "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
            },
            "Gym Class": {
                "description": "Physical education and sports activities",
                "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
                "max_participants": 30,
                "participants": ["john@mergington.edu", "olivia@mergington.edu"],
            },
            "Basketball Club": {
                "description": "Practice basketball skills and compete in school games",
                "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
                "max_participants": 20,
                "participants": [],
            },
            "Track and Field": {
                "description": "Train for running, jumping, and throwing events",
                "schedule": "Thursdays, 3:30 PM - 5:00 PM",
                "max_participants": 25,
                "participants": [],
            },
            "Art Club": {
                "description": "Explore drawing, painting, and other visual art techniques",
                "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
                "max_participants": 15,
                "participants": [],
            },
            "Drama Club": {
                "description": "Develop acting skills and perform in school productions",
                "schedule": "Mondays, 3:30 PM - 5:00 PM",
                "max_participants": 20,
                "participants": [],
            },
            "Debate Club": {
                "description": "Build research, reasoning, and public speaking skills",
                "schedule": "Thursdays, 3:30 PM - 4:30 PM",
                "max_participants": 18,
                "participants": [],
            },
            "Science Club": {
                "description": "Investigate scientific questions through experiments and projects",
                "schedule": "Fridays, 3:30 PM - 5:00 PM",
                "max_participants": 20,
                "participants": [],
            },
        }
    )


client = TestClient(app)


def test_successful_signup():
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}
    assert email in activities[activity_name]["participants"]


def test_duplicate_signup():
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student is already signed up"}
    assert activities[activity_name]["participants"].count(email) == 1


def test_unregister_participant():
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Removed {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]


def test_invalid_activity():
    # Arrange
    activity_name = "Missing Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_invalid_participant_for_unregistration():
    # Arrange
    activity_name = "Chess Club"
    email = "not-signed-up@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found"}
