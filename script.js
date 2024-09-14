document.addEventListener('DOMContentLoaded', () => {
    const patientForm = document.getElementById('patientForm');
    const patientList = document.getElementById('patientList').getElementsByTagName('tbody')[0];
    
    patientForm.addEventListener('submit', function(event) {
        event.preventDefault();

        // Get form values
        const name = document.getElementById('name').value;
        const age = document.getElementById('age').value;
        const gender = document.getElementById('gender').value;
        const diagnosis = document.getElementById('diagnosis').value;

        // Create a new row
        const newRow = patientList.insertRow();

        // Insert cells
        newRow.insertCell(0).textContent = name;
        newRow.insertCell(1).textContent = age;
        newRow.insertCell(2).textContent = gender;
        newRow.insertCell(3).textContent = diagnosis;

        // Clear form fields
        patientForm.reset();
    });
});
