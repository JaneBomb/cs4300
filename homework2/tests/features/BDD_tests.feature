Feature: register

  Scenario: register a new account
     Given we have a register page
      When we enter a <username> and <password> and click the "Sign Up" button
      Then we have a newly created account

Feature: login
  Scenario: login to an account
     Given we have a login page
      When we enter a <username> and <password> and click the "Log In" button
      Then we have enter an account

Feature: view movies
  Scenario: view all current movies
     Given we have a home page
      When we click the "All Movies" button
      Then we a list of all movies

Feature: make booking
  Scenario: make a booking for a movie
     Given we have a booking page
      When we click an available seat on the seat grid
      Then we can confirm the booking for the seat

Feature: check bookings
  Scenario: check all bookings made, including past bookings
     Given we have a user account
      When we click the account button
      Then we have a list of all bookings made