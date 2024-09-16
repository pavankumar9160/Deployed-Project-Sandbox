function validateCurrentStep() {
    let isValid = true;

    const currentFields = document.querySelectorAll('.form-control');

    currentFields.forEach(field => {
        const feedback = field.closest('.form-group').querySelector('.invalid-feedback');
        if (feedback) {

            // Custom validation for Email
            if (field.id === 'email') {
                const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
                if (field.value.trim() === "") {
                    feedback.textContent = 'Email ID is required.';
                    field.classList.remove('is-valid');
                    field.classList.add('is-invalid');
                    isValid = false;
                } else if (!emailPattern.test(field.value)) {
                    feedback.textContent = 'Invalid Email ID';
                    field.classList.remove('is-valid');
                    field.classList.add('is-invalid');
                    isValid = false;
                } else {
                    feedback.textContent = '';
                    field.classList.remove('is-invalid');
                    field.classList.add('is-valid');

                }
            }

            // Custom validation for Password
            if (field.id === 'password') {
                const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
                if (field.value.trim() === "") {
                    feedback.textContent = 'Password is required.';
                    field.classList.remove('is-valid');
                    field.classList.add('is-invalid');
                    feedback.style.display = 'block';
                    isValid = false;
                } else {
                    feedback.textContent = '';
                    field.classList.remove('is-invalid');
                    field.classList.add('is-valid');
                    feedback.style.display = 'none';

                }
            }

        }
    });

    return isValid;
}


function hasErrors() {

    const invalidFields = document.querySelectorAll('.is-invalid');
    return invalidFields.length > 0;
}


document.getElementById('submit').addEventListener('click', function(event) {
    const submitButton = event.target;
    if (!validateCurrentStep() || hasErrors()) {
        event.preventDefault();
        event.stopPropagation();
    }
});


onInputValidation();


function onInputValidation() {
    const currentFields = document.querySelectorAll('.form-control');
    currentFields.forEach(field => {

        field.addEventListener('input', function() {


            const feedback = field.closest('.form-group').querySelector('.invalid-feedback');
            if (feedback) {

                // Custom validation for Email
                if (field.id === 'email') {
                    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
                    if (field.value.trim() === "") {
                        feedback.textContent = 'Email ID is required.';
                        field.classList.remove('is-valid');
                        field.classList.add('is-invalid');
                        isValid = false;
                    } else if (!emailPattern.test(field.value)) {
                        feedback.textContent = 'Invalid Email ID';
                        field.classList.remove('is-valid');
                        field.classList.add('is-invalid');
                        isValid = false;
                    } else {
                        feedback.textContent = '';
                        field.classList.remove('is-invalid');
                        field.classList.add('is-valid');

                    }
                }

                // Custom validation for Password
                else if (field.id === 'password') {
                    const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
                    if (field.value.trim() === "") {
                        feedback.textContent = 'Password is required.';
                        field.classList.remove('is-valid');
                        field.classList.add('is-invalid');
                        feedback.style.display = 'block';
                        isValid = false;
                    } else if (!passwordPattern.test(field.value)) {
                        feedback.textContent = 'Password should contain atleast 8 characters.';
                        field.classList.remove('is-valid');
                        field.classList.add('is-invalid');
                        feedback.style.display = 'block';
                        isValid = false;
                    } else {
                        feedback.textContent = '';
                        field.classList.remove('is-invalid');
                        field.classList.add('is-valid');
                        feedback.style.display = 'none';

                    }
                } else {
                    feedback.textContent = '';
                    field.classList.remove('is-invalid');
                    field.classList.add('is-valid');
                }

            };
        });


    });
}


// toggle password visibility//
function togglePasswordVisibility(fieldId) {
    const field = document.getElementById(fieldId);
    const icon = field.nextElementSibling.querySelector('i');
    if (field.type === "password") {
        field.type = "text";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
    } else {
        field.type = "password";
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
    }
}