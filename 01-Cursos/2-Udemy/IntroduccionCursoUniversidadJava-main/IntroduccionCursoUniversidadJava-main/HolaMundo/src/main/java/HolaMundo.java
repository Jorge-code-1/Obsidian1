
import java.util.Scanner;




public class HolaMundo {

    public static void main(String[] args) {
       
        var scanner = new Scanner(System.in);
        System.out.println("Ingrese el numero del mes : ");
     var mes=scanner.nextInt();
     String estacion = null;
     
     switch(mes){
         case 1: case 2: case 3:
             estacion = "verano";
             break;
         case 4: case 5: case 6:
              estacion = "otoño";
             break;
         case 7: case 8: case 9:
              estacion= "invierno";
             break;
         case 10: case 11: case 12:
             estacion = "primavera";
             break;
         default:
             estacion ="Mes incorrecto";
             
     }
        System.out.println("estacion =  " + estacion  + " para el mes :  " + mes);
       
}
}
