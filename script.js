document.addEventListener('DOMContentLoaded', () => {
    const patientForm = document.getElementById('patientForm');
    const patientList = document.getElementById('patientList').getElementsByTagName('tbody')[0];
    
    const appointmentForm = document.getElementById('appointmentForm');
    const appointmentList = document.getElementById('appointmentList').getElementsByTagName('tbody')[0];
    
    // Fetch and display patients
    function fetchPatients() {
        fetch('/patients')
            .then(response => response.json())
            .then(data => {
                patientList.innerHTML = '';
                data.forEach(patient => {
                    const newRow = patientList.insertRow();
                    newRow.insertCell(0).textContent = patient.name;
                    newRow.insertCell(1).textContent = patient.age;
                    newRow.insertCell(2).textContent = patient.gender;
                    newRow.insertCell(3).textContent = patient.diagnosis;
                });
            });
    }
    
    // Fetch and display appointments
    function fetchAppointments() {
        fetch('/appointments')
            .then(response => response.json())
            .then(data => {
                appointmentList.innerHTML = '';
                data.forEach(appointment => {
                    const newRow = appointmentList.insertRow();
                    newRow.insertCell(0).textContent = appointment.patientName;
                    newRow.insertCell(1).textContent = appointment.date;
                    newRow.insertCell(2).textContent = appointment.time;
                    newRow.insertCell(3).textContent = appointment.doctor;
                });
            });
    }

    // Handle patient form submission
    patientForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const age = document.getElementById('age').value;
        const gender = document.getElementById('gender').value;
        const diagnosis = document.getElementById('diagnosis').value;

        fetch('/patients', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, age, gender, diagnosis })
        }).then(() => {
            fetchPatients();
            patientForm.reset();
        });
    });

    // Handle appointment form submission
    appointmentForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const patientName = document.getElementById('patientName').value;
        const date = document.getElementById('date').value;
        const time = document.getElementById('time').value;
        const doctor = document.getElementById('doctor').value;

        fetch('/appointments', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ patientName, date, time, doctor })
        }).then(() => {
            fetchAppointments();
            appointmentForm.reset();
        });
    });

    // Initial fetch to display data
    fetchPatients();
    fetchAppointments();
});
