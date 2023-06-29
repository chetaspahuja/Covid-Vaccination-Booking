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

   Code Snippet: [admin_home.html](/path/to/admin_home.html)

2. **User Booking**

   - Users can select a date to view the available vaccination centers and their slots for that date.
   - Users can book a slot at their preferred vaccination center.

   Code Snippet: [selectDate.html](/path/to/selectDate.html), [booking.html](/path/to/booking.html)

3. **Admin Authentication and Logout**

   - Admins can log in to the application using their username and password.
   - Admins can log out of the application.

   Code Snippet: [login.html](/path/to/login.html)

4. **Updating Slots for Vaccination Centers**

   - Admins can update the number of available slots for a specific vaccination center and date.
   - If the record for the given date doesn't exist, a new record will be created.

   Code Snippet: [update_slots.html](/path/to/update_slots.html)

## License

This project is licensed under the [MIT License](LICENSE).
