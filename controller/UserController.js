function UserController(){
    
    this.setUserJson = (reg) => {
        let userJson = null;

        userJson = {
            userId: reg.id,
            userEmail: reg.email,
            userName: reg.name,
            userPass: reg.pass,
            confPass: reg.confPass
        };
    }

    let json;

    this.setRegisterJson = (obj) => {
        json = JSON.stringify(obj);
    }

    this.getRegisterJson = () => {
        console.log(json);
        return json;
    }

    // this.getUserJson = (id) => {
        
    //     let user = new UserModel();
    //     let userJson = null;

    //     userJson = user.getUserJsonModel(id);

    //     return userJson;
    // }

    function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
        if (x == "") {
            alert("Name must be filled out");
            return false;
        }
    }

    function checkPassword(form) { 
        password1 = form.password1.value; 
        password2 = form.password2.value; 

        // If password not entered 
        if (password1 == '') 
            alert ("Please enter Password"); 
              
        // If confirm password not entered 
        else if (password2 == '') 
            alert ("Please enter confirm password"); 
              
        // If Not same return False.     
        else if (password1 != password2) { 
            alert ("\nPassword did not match: Please try again...") 
            return false; 
        } 

        // If same return True. 
        else{ 
            alert("Password Match: Welcome to GeeksforGeeks!") 
            return true; 
        } 
    } 

}

let hey = {
    email: "pedrcg835@gmail.com",
    name : "Pedro",
    pass: "qwerty",
    confPass: "qwerty"
};

// let user1 = new UserController(hey);

// console.log(user1.getUserJson());