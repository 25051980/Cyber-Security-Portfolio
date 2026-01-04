
-- SECTION 4 – Full Journey Sample Data

-- STEP 1: Add Membership Plans
INSERT INTO Memberships (MembershipID, MembershipType, Benefits)
VALUES 
(1, 'Basic', 'Access to gym equipment and group classes'),
(2, 'Premium', 'Includes personal training, sauna, and all classes');

-- STEP 2: Add Members
INSERT INTO Members (MemberID, FirstName, LastName, DOB, Email, Phone, Address, MembershipID, StartDate, EndDate)
VALUES
(1, 'Maria', 'Silva', '1990-03-15', 'maria.silva@email.com', '555-10203', 'Av. Brasil, 45', 2, '2025-06-14', '2026-06-01'),
(2, 'João', 'Costa', '1985-08-20', 'joao.costa@email.com', '555-20804', 'Rua Verde, 12', 1, '2025-06-14', '2026-06-01');

-- STEP 3: Add Trainers
INSERT INTO Trainers (TrainerID, FirstName, LastName, Specialty)
VALUES
(1, 'Carlos', 'Souza', 'Yoga'),
(2, 'Ana', 'Martins', 'CrossFit');

-- STEP 4: Add Classes
INSERT INTO Classes (ClassID, ClassName, Description)
VALUES
(1, 'Morning Yoga', 'Relaxing yoga for all levels'),
(2, 'Power CrossFit', 'High intensity functional training');

-- STEP 5: Schedule Classes
INSERT INTO ClassSchedule (ScheduleID, ClassID, TrainerID, ScheduledDateTime)
VALUES
(1, 1, 1, '2025-06-21 20:03:44'),
(2, 2, 2, '2025-06-21 20:03:44');

-- STEP 6: Members Book Classes
INSERT INTO Bookings (BookingID, MemberID, ScheduleID, BookingDate, AttendanceStatus)
VALUES
(1, 1, 1, '2025-06-16', 'Attended'),
(2, 2, 2, '2025-06-16', 'Missed');

-- STEP 7: Record Payments
INSERT INTO Payments (PaymentID, MemberID, PaymentDate, Amount, Status)
VALUES
(1, 1, '2025-06-14', 300.00, 'Paid'),
(2, 2, '2025-06-14', 150.00, 'Pending');

-- STEP 8: Demonstration Queries

-- a) Get all class bookings with member and trainer details
SELECT m.FirstName AS Member, c.ClassName, cs.ScheduledDateTime, b.AttendanceStatus, t.FirstName AS Trainer
FROM Bookings b
JOIN Members m ON b.MemberID = m.MemberID
JOIN ClassSchedule cs ON b.ScheduleID = cs.ScheduleID
JOIN Classes c ON cs.ClassID = c.ClassID
JOIN Trainers t ON cs.TrainerID = t.TrainerID;

-- b) View payments made by members
SELECT m.FirstName, p.PaymentDate, p.Amount, p.Status
FROM Payments p
JOIN Members m ON p.MemberID = m.MemberID;

-- c) Show full schedule for each trainer
SELECT t.FirstName AS Trainer, c.ClassName, cs.ScheduledDateTime
FROM Trainers t
JOIN ClassSchedule cs ON t.TrainerID = cs.TrainerID
JOIN Classes c ON cs.ClassID = c.ClassID
ORDER BY cs.ScheduledDateTime;
