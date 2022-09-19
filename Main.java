import AC.Analisador;
import AC.Token;
import AC.Analisador1;
public class Main {
    public static void main(String args[]) {
        Analisador1 analex = new Analisador1("teste.txt");

        Token token = null;

        do {
            token = analex.percorreToken();

            if(token != null){
                System.out.println(token);
            }
            
        } while (token != null);
    }
}