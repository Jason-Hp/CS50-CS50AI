-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Information on the day of crime
select * from crime_scene_reports WHERE month = 7 AND day = 28 AND street = "Humphrey Street"
-- Crime took place at 10:15am at the bakery,
-- | 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
| 5P2BI95       |
| 94KL13X       |
| 6P58WS2       |
| 4328GD8       |
| G412CB7       |
| L93JTIZ       |
| 322W7JE       |
| 0NTHK55       |

--| 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
 select account_number from atm_transactions WHERE month = 7 and day =28 and atm_location= "Leggett Street" and transaction_type = "withdraw"
| 28500762       |
| 28296815       |
| 76054385       |
| 49610011       |
| 16153065       |
| 25506511       |
| 81061156       |
| 26013199
--| 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
+----------------+----------------+
|     caller     |    receiver    |
+----------------+----------------+
| (130) 555-0289 | (996) 555-8899 |
| (499) 555-9472 | (892) 555-8872 |
| (367) 555-5533 | (375) 555-8161 |
| (499) 555-9472 | (717) 555-1342 |
| (286) 555-6063 | (676) 555-6554 |
| (770) 555-1861 | (725) 555-3243 |
| (031) 555-6622 | (910) 555-3251 |
| (826) 555-1652 | (066) 555-9701 |
| (338) 555-6650 | (704) 555-2131 |
+----------------+----------------+
select caller, receiver from phone_calls where month = 7 AND day =28 and duration<60;
select name from bakery_security_logs
   ...> JOIN people ON bakery_security_logs.license_plate = people.license_plate
   ...> WHERE month = 7 AND day = 28 AND hour = 10 AND minute>=15 AND minute<=25
   ...> INTERSECT
select name from atm_transactions
 JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number
 JOIN people ON bank_accounts.person_id = people.id
 WHERE atm_transactions.month = 7 AND atm_transactions.day = 28 AND atm_transactions.atm_location = "Leggett Street" AND atm_transactions.transaction_type = "withdraw"

+-------+
| name  |
+-------+
| Bruce |
| Diana |
| Iman  |
| Luca  |
+-------+

select name from flights JOIN passengers ON flights.id = passengers.flight_id JOIN people ON passengers.passport_number = people.passport_number WHERE flights.month = 7 AND flights.day = 29 AND (name = "Bruce" OR name = "Diana" OR name = "Iman")

sqlite> select name from phone_calls
   ...> JOIN people on phone_calls.receiver = people.phone_number
   ...> WHERE phone_calls.receiver = (
   ...> SELECT receiver from phone_calls WHERE day = 28 AND duration<60 AND caller = (
   ...> SELECT phone_number from people WHERE name = "Bruce"));
