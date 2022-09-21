import AC.Token;
import AC.Analisador2;
public class Main2 {
    public static void main(String args[]) {
        Analisador2 analex = new Analisador2("teste.txt");

        Token token = null;

        do {
            token = analex.percorreToken();

            if(token != null){
                System.out.println(token);
            }
            
        } while (token != null);
    }
}