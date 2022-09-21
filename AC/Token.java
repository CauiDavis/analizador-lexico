package AC;

public class Token {
    public static final int identificador = 1;

    private String valor;
    private int tipo;

    public Token(String valor, int tipo){
        super();
        this.valor = valor;
        this.tipo = tipo;
    }

    public Token(){
        super();
    }

    public void setTipo(int t){
        this.tipo = t;
    }

    public void setValor(String v){
        this.valor = v;
    }

    public int getTipo(){
        return this.tipo;
    }

    public String getValor(){
        return this.valor;
    }
    
    @Override
    public String toString(){
        if(tipo == 1){
        return "Token{" +
                "type=" + tipo +
                ",identificador, text='" + valor + '\'' +
                '}';
        }
        else{
            return "Token{" +
                "type=" + tipo +
                ", text='" + valor + '\'' +
                '}';
        }
    }
}
