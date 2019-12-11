function OrganizationController(){
    
    this.becomeOrg = async () => {
        let band = false;
        let userEmail;
        let jsonData;
        let orgUser = {};
        let conn = new UserCRUD();

        userEmail = localStorage.getItem('email');

        jsonData = await conn.getUsersDB();

        for(let i = 0; i < jsonData.length; i++){
            if(userEmail == jsonData[i].email){
                orgUser = jsonData[i];
                orgUser.is_org = true;
                band = true;
            }
        }

        if(band){
            console.log(orgUser);
            conn.updateUser(orgUser);
        }

    }
}