import java.util.Scanner;
class CredentialException extends Exception{
    public CredentialException(String s){
        super(s);
    }
}
class pro19{
    public static void main(String[] args) {
        String username = "joel";
        String password = "321";
        Scanner scn = new Scanner(System.in);
        System.out.print("Username : ");
        String user = scn.next();
        System.out.print("Password : ");
        String pass = scn.next();
        try{
            if( user.equals(username) && pass.equals(password) ){
                System.out.println("Access Granted");
            }else{
                throw new CredentialException("Invalid Credentials");
            }
        }catch(CredentialException e){
            System.out.println(e.getMessage());
        }
    }
}
