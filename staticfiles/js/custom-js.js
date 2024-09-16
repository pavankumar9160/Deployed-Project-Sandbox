 // Form Validation

 // Controlling Forward And BackWard Buttons
 let currentStep = 1;
 const totalSteps = 4;

 document.getElementById('forward-button').addEventListener('click', function(event) {
     if (!validateCurrentStep() || hasErrors()) {
         event.preventDefault();
         event.stopPropagation();
     } else {
         if (currentStep < totalSteps) {
             showStep(currentStep + 1);
         }
     }
 });

 document.getElementById('backward-button').addEventListener('click', function() {
     if (currentStep > 1) {
         showStep(currentStep - 1);
     }
 });

 document.getElementById('register-btn').addEventListener('click', function(event) {
     const submitButton = event.target;
     if (!validateCurrentStep() || hasErrors()) {
         event.preventDefault();
         event.stopPropagation();


     } else {
         console.log("Form submitted");



     }
 });

 function showStep(step) {
     for (let i = 1; i <= totalSteps; i++) {
         document.getElementById(`step-${i}`).style.display = 'none';
     }

     document.getElementById(`step-${step}`).style.display = 'block';

     currentStep = step;

     if (currentStep === 1) {
         document.getElementById('backward-button').style.display = 'none';
     } else {
         document.getElementById('backward-button').style.display = 'block';
     }

     if (currentStep === totalSteps) {
         document.getElementById('forward-button').style.display = 'none';
         document.getElementById('register-btn').style.display = 'block';
     } else {
         document.getElementById('forward-button').style.display = 'block';
         document.getElementById('register-btn').style.display = 'none';
     }

     onInputValidation();
 }



 function validateCurrentStep() {
     let isValid = true;

     const currentFields = document.querySelectorAll(`#step-${currentStep} .form-control`);
     //  const submitbutton = document.getElementById('register-btn');
     //  submitbutton.disabled = false;
     currentFields.forEach(field => {
         const feedback = field.closest('.form-group').querySelector('.invalid-feedback');
         if (feedback) {

             // Custom Validation For FirstName

             if (field.id === 'firstname') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'First Name is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else {
                     feedback.textContent = '';

                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');
                 }
             }

             // Custom Validation For FirstName

             if (field.id === 'lastname') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Last Name is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else {
                     feedback.textContent = '';

                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');
                 }
             }

             // Custom validation for Date of birth

             if (field.id === 'dateofbirth') {
                 const today = new Date().toISOString().split('T')[0];
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Date of Birth is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else if (field.value > today) {
                     feedback.textContent = 'Date of Birth cannot be in the future.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else {
                     feedback.textContent = '';

                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');
                 }
             }

             // Custom Validation For BloodGroup

             if (field.id === 'bloodgroup') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Blood Group is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else {
                     feedback.textContent = '';

                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');
                 }
             }

             // Custom Validation For Marital Status

             if (field.id === 'maritalstatus') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Marital Status is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');
                     toggleMarriageDate(field.value);
                 }
             }



             // Custom validation for Marriage Date

             if (field.id === 'marriagedate' && document.getElementById('maritalstatus').value === '1') {
                 const today = new Date().toISOString().split('T')[0];
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Marriage Date is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else if (field.value > today) {
                     feedback.textContent = 'Marriage Date cannot be in the future.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else {
                     feedback.textContent = '';

                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');
                 }
             }


             // Custom validation for Current Address
             if (field.id === 'currentaddress') {

                 if (field.value.trim() === "") {
                     feedback.textContent = 'Current Address is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else if (field.value.length < 10) {
                     feedback.textContent = 'Address is too short.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else {
                     feedback.textContent = '';

                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');

                 }

             }

             // Custom validation for Phone Number (exactly 10 digits)
             if (field.id === 'phonenumber') {
                 const phoneRegex = /^[0-9]{10}$/; // Regular expression for 10 digits

                 if (field.value.trim() === "") {
                     feedback.textContent = 'Phone Number is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else if (!phoneRegex.test(field.value)) {
                     feedback.textContent = 'Phone number should contain 10 digits.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');

                 }

             }
             // Custom Validation For Upload Image

             if (field.id === 'uploadimage') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Image   is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');
                 }
             }
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
             }

             // Custom validation for Confirm Password
             if (field.id === 'confirmpassword') {
                 const passwordField = document.getElementById('password');
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Confirm password is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     feedback.style.display = 'block';
                     isValid = false;
                 } else if (field.value !== passwordField.value) {
                     feedback.textContent = 'Password and confirm password do not match.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     feedback.style.display = 'block';
                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');
                     feedback.style.display = 'none ';
                 }
             }

             // Custom Validation For Highest Qualification

             if (field.id === 'highestqualification') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Highest Qualification is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');
                 }
             }


             // Custom Validation For Role Type

             if (field.id === 'roletype') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Role type is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');
                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');
                 }
             }

             // Custom Validation For Pan card Image

             if (field.id === 'uploadpan') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Pan card image is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');

                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');

                 }
             }


             // Custom validation for PAN Number
             if (field.id === 'pannumber') {
                 const panPattern = /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/;
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Pan Number is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');

                     isValid = false;
                 } else if (!panPattern.test(field.value)) {
                     feedback.textContent = 'Invalid Pan Number.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');

                     isValid = false;

                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');

                 }
             }



             // Custom Validation For Bank Name

             if (field.id === 'bankname') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Bank Name is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');

                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');

                 }
             }

             // Custom validation for Bank Account Number
             if (field.id === 'bankaccountnumber') {
                 const accountPattern = /^[0-9]{8,16}$/; // Example: 8 to 16 digits
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Bank Account Number is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');

                     isValid = false;
                 } else if (!accountPattern.test(field.value)) {
                     feedback.textContent = 'Invalid Bank Account Number.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');

                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');


                 }
             }

             // Custom validation for Bank IFSC Code
             if (field.id === 'ifsccode') {
                 const ifscPattern = /^[A-Z]{4}0[A-Z0-9]{6}$/;
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Ifsc Code is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');

                     isValid = false;
                 } else if (!ifscPattern.test(field.value)) {
                     feedback.textContent = 'Invalid Ifsc Code.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');

                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');


                 }
             }

             // Custom Validation For  Employee Name

             if (field.id === 'employeename') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Employee Name is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');

                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');

                 }
             }

             // Custom Validation For Aadhar card image

             if (field.id === 'uploadaadharcard') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'Aadhar card image is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');

                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');

                 }
             }
             // Custom Validation For system IP Address

             if (field.id === 'systemipaddress') {
                 if (field.value.trim() === "") {
                     feedback.textContent = 'System IP Address is required.';
                     field.classList.remove('is-valid');
                     field.classList.add('is-invalid');

                     isValid = false;
                 } else {
                     feedback.textContent = '';
                     field.classList.remove('is-invalid');
                     field.classList.add('is-valid');

                 }
             }

         }
     });

     return isValid;
 }

 function hasErrors() {

     const invalidFields = document.querySelectorAll(`#step-${currentStep} .is-invalid`);
     return invalidFields.length > 0;
 }

 function onInputValidation() {
     const currentFields = document.querySelectorAll(`#step-${currentStep} .form-control`);
     currentFields.forEach(field => {

         field.addEventListener('input', function() {


             const feedback = field.closest('.form-group').querySelector('.invalid-feedback');
             if (feedback) {




                 // Custom Validation For FirstName

                 if (field.id === 'firstname') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'First Name is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';

                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }

                 // Custom Validation For FirstName
                 else if (field.id === 'lastname') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Last Name is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';

                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }

                 // Custom validation for Date of birth
                 else if (field.id === 'dateofbirth') {
                     const today = new Date().toISOString().split('T')[0];
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Date of Birth is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else if (field.value > today) {
                         feedback.textContent = 'Date of Birth cannot be in the future.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';

                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }

                 // Custom Validation For BloodGroup
                 else if (field.id === 'bloodgroup') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Blood Group is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';

                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }

                 // Custom Validation For Marital Status
                 else if (field.id === 'maritalstatus') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Marital Status is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');

                         toggleMarriageDate(field.value);
                     }
                 }



                 // Custom validation for Marriage Date
                 else if (field.id === 'marriagedate' && document.getElementById('maritalstatus').value === '1') {
                     const today = new Date().toISOString().split('T')[0];
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Marriage Date is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else if (field.value > today) {
                         feedback.textContent = 'Marriage Date cannot be in the future.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';

                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }


                 // Custom validation for Current Address
                 else if (field.id === 'currentaddress') {

                     if (field.value.trim() === "") {
                         feedback.textContent = 'Current Address is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else if (field.value.length < 10) {
                         feedback.textContent = 'Address is too short.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';

                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');

                     }

                 }

                 // Custom validation for Phone Number (exactly 10 digits)
                 else if (field.id === 'phonenumber') {
                     const phoneRegex = /^[0-9]{10}$/; // Regular expression for 10 digits

                     if (field.value.trim() === "") {
                         feedback.textContent = 'Phone Number is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else if (!phoneRegex.test(field.value)) {
                         feedback.textContent = 'Phone number should contain 10 digits.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');

                     }

                 }
                 // Custom Validation For Upload Image
                 else if (field.id === 'uploadimage') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Image   is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }
                 // Custom validation for Email
                 else if (field.id === 'email') {
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
                 }

                 // Custom validation for Confirm Password
                 else if (field.id === 'confirmpassword') {
                     const passwordField = document.getElementById('password');
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Confirm password is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         feedback.style.display = 'block';
                         isValid = false;
                     } else if (field.value !== passwordField.value) {
                         feedback.textContent = 'Password and confirm password do not match.';
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

                 // Custom Validation For Highest Qualification
                 else if (field.id === 'highestqualification') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Highest Qualification is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }


                 // Custom Validation For Role Type
                 else if (field.id === 'roletype') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Role type is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }

                 // Custom Validation For Pan card Image
                 else if (field.id === 'uploadpan') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Pan card image is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }


                 // Custom validation for PAN Number
                 else if (field.id === 'pannumber') {
                     const panPattern = /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/;
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Pan Number is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else if (!panPattern.test(field.value)) {
                         feedback.textContent = 'Invalid Pan Number.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');

                     }
                 }



                 // Custom Validation For Bank Name
                 else if (field.id === 'bankname') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Bank Name is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }

                 // Custom validation for Bank Account Number
                 else if (field.id === 'bankaccountnumber') {
                     const accountPattern = /^[0-9]{8,16}$/; // Example: 8 to 16 digits
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Bank Account Number is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else if (!accountPattern.test(field.value)) {
                         feedback.textContent = 'Invalid Bank Account Number.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');

                     }
                 }

                 // Custom validation for Bank IFSC Code
                 else if (field.id === 'ifsccode') {
                     const ifscPattern = /^[A-Z]{4}0[A-Z0-9]{6}$/;
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Ifsc Code is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else if (!ifscPattern.test(field.value)) {
                         feedback.textContent = 'Invalid Ifsc Code.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');

                     }
                 }

                 // Custom Validation For  Employee Name
                 else if (field.id === 'employeename') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Employee Name is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }

                 // Custom Validation For Aadhar card image
                 else if (field.id === 'uploadaadharcard') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'Aadhar card image is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
                     }
                 }
                 // Custom Validation For system IP Address
                 else if (field.id === 'systemipaddress') {
                     if (field.value.trim() === "") {
                         feedback.textContent = 'System IP Address is required.';
                         field.classList.remove('is-valid');
                         field.classList.add('is-invalid');
                         isValid = false;
                     } else {
                         feedback.textContent = '';
                         field.classList.remove('is-invalid');
                         field.classList.add('is-valid');
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

 // Function to toggle visibility of Marriage Date field
 function toggleMarriageDate(status) {
     const marriageDateField = document.getElementById('marriagedate-field');
     const currentaddressField = document.getElementById('currentaddress-field');
     console.log(currentaddressField.classList); // Before removing classes

     const phonenumberField = document.getElementById('phonenumber-field'); // Container for the marriage date
     if (status === '1') {
         marriageDateField.style.display = "block";
         if (currentaddressField.classList.contains('col-md-6')) {
             currentaddressField.classList.remove('col-md-6');
         }
         if (phonenumberField.classList.contains('col-md-6')) {
             phonenumberField.classList.remove('col-md-6');
         }
         currentaddressField.classList.add('col-md-4')
         phonenumberField.classList.add('col-md-4');
     } else {

         marriageDateField.style.display = "none";
         // Clear the marriage date field value when hiding it
         document.getElementById('marriagedate').value = '';
         if (currentaddressField.classList.contains('col-md-4')) {
             currentaddressField.classList.remove('col-md-4');
         }
         if (phonenumberField.classList.contains('col-md-4')) {
             phonenumberField.classList.remove('col-md-4');
         }
         currentaddressField.classList.add('col-md-6')
         phonenumberField.classList.add('col-md-6');
     }
 }

 // Initialize the first step
 showStep(1);

 // Load the marital status from localStorage on page load and toggle marriage date field
 document.addEventListener("DOMContentLoaded", function() {
     const maritalStatus = localStorage.getItem('maritalstatus'); // Retrieve marital status from localStorage

     if (maritalStatus) {
         // Set the marital status field to the stored value
         document.getElementById('maritalstatus').value = maritalStatus;

         // Toggle the marriage date field based on the saved marital status
         toggleMarriageDate(maritalStatus);
     }

     // Add event listener to marital status field to toggle marriage date field on change
     document.getElementById('maritalstatus').addEventListener('change', function() {
         const status = this.value;
         localStorage.setItem('maritalstatus', status); // Save marital status to localStorage
         toggleMarriageDate(status); // Toggle marriage date field based on status
     });
 });



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



 // Function to fetch the user's IP address
 function fetchIPAddress() {
     fetch('https://api.ipify.org?format=json')
         .then(response => response.json())
         .then(data => {
             // Set the IP address in the input field
             document.getElementById('systemipaddress').value = data.ip;
         })
         .catch(error => {
             console.error('Error fetching IP address:', error);
         });
 }

 // Call the function when the page loads
 window.onload = function() {
     fetchIPAddress();
 };

 document.addEventListener("DOMContentLoaded", function() {
     // Function to save data to localStorage
     function saveData() {
         const fields = [
             "firstname", "lastname", "dateofbirth", "bloodgroup", "maritalstatus",
             "marriagedate", "currentaddress", "phonenumber", "email", "password",
             "confirmpassword", "highestqualification", "roletype", "pannumber",
             "bankname", "bankaccountnumber", "ifsccode", "employeename", "systemipaddress"
         ];

         fields.forEach(fieldId => {
             const field = document.getElementById(fieldId);
             if (field) {
                 if (field.type === 'radio') {
                     if (field.checked) {
                         localStorage.setItem(fieldId, field.value);
                     }
                 } else {
                     localStorage.setItem(fieldId, field.value);
                 }
             }
         });
     }





     // Function to load data from localStorage
     function loadData() {
         const fields = [
             "firstname", "lastname", "dateofbirth", "bloodgroup", "maritalstatus",
             "marriagedate", "currentaddress", "phonenumber", "email", "password",
             "confirmpassword", "highestqualification", "roletype", "pannumber",
             "bankname", "bankaccountnumber", "ifsccode", "employeename", "systemipaddress"
         ];

         fields.forEach(fieldId => {
             const savedValue = localStorage.getItem(fieldId);
             const field = document.getElementById(fieldId);
             if (field && savedValue) {
                 if (field.type === 'radio') {
                     field.checked = (field.value === savedValue);
                 } else {
                     field.value = savedValue;
                 }
             }
         });
     }

     // Attach event listeners to the input fields to save data on input
     const inputFields = [
         "firstname", "lastname", "dateofbirth", "bloodgroup", "maritalstatus",
         "marriagedate", "currentaddress", "phonenumber", "email", "password",
         "confirmpassword", "highestqualification", "roletype", "pannumber",
         "bankname", "bankaccountnumber", "ifsccode", "employeename", "systemipaddress"
     ];

     inputFields.forEach(fieldId => {
         const field = document.getElementById(fieldId);
         if (field) {
             field.addEventListener("input", saveData);
         }
     });

     // Load the data on page load
     loadData();
 });