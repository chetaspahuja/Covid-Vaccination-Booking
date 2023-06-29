# Covid-Vaccination-Booking
# COVID-19 Vaccination Management Application

This is a COVID-19 Vaccination Management Application that provides features for administrators to manage vaccination centers, update available slots, and add new centers. It also allows users to select a date and book vaccination slots.

## Technologies Used

- Django: A Python web framework used for backend development.
- HTML/CSS: Used for frontend development and styling.
- SQLite: The database engine used for data storage.

## Functionality and Code Snippets

1. **Vaccination Center Management**

   - Admins can view a list of vaccination centers, including their names, center names, addresses, and available slots.
   - Admins can update the number of available slots for a specific center and date.
   - Admins can delete a vaccination center from the list.
   - Admins can add a new vaccination center to the list.

2. **User Booking**

   - Users can select a date to view the available vaccination centers and their slots for that date.
   - Users can book a slot at their preferred vaccination center.

3. **Admin Authentication and Logout**

   - Admins can log in to the application using their username and password.
   - Admins can log out of the application.

4. **Updating Slots for Vaccination Centers**

   - Admins can update the number of available slots for a specific vaccination center and date.
   - If the record for the given date doesn't exist, a new record will be created.

## License

This project is licensed under the [MIT License](LICENSE).
