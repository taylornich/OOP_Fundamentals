from event import Event

def main():
    specific_event = Event("Comic Con", "07-23-2024")

    print(f"The initial participant count for {specific_event.name}: {specific_event.get_participant_count()}")

    specific_event.add_participant()
    specific_event.add_participant()
    specific_event.add_participant()
    specific_event.add_participant()

    print(f"The updated participant count for {specific_event.name} on {specific_event.date}: {specific_event.get_participant_count()}")

if __name__ == "__main__":
    main()