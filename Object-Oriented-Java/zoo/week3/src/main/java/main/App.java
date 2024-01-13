/**
 * Hiltunen Teemu; 06.02.2023
 */

/**
 * Zoo program, needs to be able to add animals, list them and make them run. Simple as that.
 */


package main;

import java.util.Scanner;



public class App {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Anna eläintarhalle nimi:");
        String zooName = input.nextLine();

        Zoo zoo = new Zoo(zooName);

        boolean exit = false;
        while (!exit) {

            System.out.println("1) Luo uusi eläin, 2) Listaa kaikki eläimet, 3) Juoksuta eläimiä, 0) Lopeta ohjelma");

            if (input.hasNext()) {
                int i = 0;
                String stringInput = input.nextLine();
                i = Integer.parseInt(stringInput);

                switch (i) {
                    case 1:

                        System.out.println("Mikä laji?");
                        String species = input.nextLine();

                        System.out.println("Anna eläimen nimi:");
                        String name = input.nextLine();

                        System.out.println("Anna eläimen ikä:");
                        String ageInput = input.nextLine();
                        int age = Integer.parseInt(ageInput);

                        Animal animal = new Animal(species, name, age);
                        zoo.addAnimal(animal);
                        break;

                    case 2:
                        zoo.listAnimals();
                        break;

                    case 3:
                        System.out.println("Kuinka monta kierrosta?");
                        int rounds = Integer.parseInt(input.nextLine());
                        zoo.runAnimals(rounds);
                        break;

                    case 0:

                        System.out.println("Kiitos ohjelman käytöstä.");
                        exit = true;
                        break;

                    default:
                        System.out.println("Syöte oli väärä");
                }
            }
        }
        input.close();
    }

}

// End of File
