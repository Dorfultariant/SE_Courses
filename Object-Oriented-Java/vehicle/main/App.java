package main;

import java.util.Scanner;
import java.util.ArrayList;


public class App {
    public static void main(String[] args) {

        ArrayList<Vehicle> vehicles = new ArrayList<>();
        

        Scanner input = new Scanner(System.in);
        int choice = 0;
        String stringInput;
    
        Boolean exit = false;
        while(exit != true) {

            // Menu:
            System.out.print("1) Luo uusi kulkuneuvo, 2) Listaa kulkuneuvot ");
            System.out.print("3) Aja autoja, 4) Lennä lentokoneita, ");
            System.out.println("5) Seilaa laivoja, 0) Lopeta ohjelma");

            if(input.hasNext()) {
                // Choice input from user:
                stringInput = input.nextLine();
                choice = Integer.parseInt(stringInput);

                switch (choice) {
                    case 1:  // Create new vehicle:
                        System.out.print("Minkä kulkuneuvon haluat rakentaa? ");
                        System.out.println("1) auto, 2) lentokone, 3) laiva");
                        int intInput = Integer.parseInt(input.nextLine());

                        System.out.println("Anna kulkuneuvon valmistaja:");
                        String manufacturer = input.nextLine();

                        System.out.println("Anna kulkuneuvon malli:");
                        String model = input.nextLine();

                        System.out.println("Anna kulkuneuvon huippunopeus:");
                        int maxSpeed = Integer.parseInt(input.nextLine());

                        if (intInput == 1) {
                            Car car = new Car(manufacturer, model, maxSpeed);
                            vehicles.add(car);

                        } else if (intInput == 2) {
                            Plane plane = new Plane(manufacturer, model, maxSpeed);
                            vehicles.add(plane);

                        } else if (intInput == 3) {
                            Ship ship = new Ship(manufacturer, model, maxSpeed);
                            vehicles.add(ship);

                        } else {
                            System.out.println("Tuntematon valinta, yritä uudestaan.");
                        }
                        break;

                    case 2: // List vehicles:
                        
                        
                        for (Vehicle vehicle : vehicles) {
                            System.out.println(vehicle.type + ": " + vehicle.manufacturer + " " + vehicle.model);
                            System.out.println("Moottori: " + vehicle.motor + " " + vehicle.power + "kW");
                            System.out.println("Huippunopeus: " + vehicle.maxSpeed + "km/h");
                            System.out.println();
                        }
                        break;
                    case 3: // drive cars:
                        for (Vehicle vehicle : vehicles) {
                            if (vehicle instanceof Car) {
                                ((Car)vehicle).drive();
                            }
                            
                        }
                        break;

                    case 4: // fly planes:
                        for (Vehicle vehicle : vehicles) {
                            if (vehicle instanceof Plane) {
                                ((Plane)vehicle).fly();
                            }
                        }
                        break;
                    case 5: // sail ships:
                        for (Vehicle vehicle : vehicles) {
                            if (vehicle instanceof Ship) {
                                ((Ship)vehicle).sail();
                            }
                        }
                        break;
                    case 0:
                        System.out.println("Kiitos ohjelman käytöstä.");
                        exit = true;
                        break;        
                    default:
                        System.out.println("Tuntematon valinta, yritä uudestaan.");
                        break;
                }
            }
        }
        input.close();   
    }    
}