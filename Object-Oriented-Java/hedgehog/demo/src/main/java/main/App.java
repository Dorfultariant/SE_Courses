/**
 * Hiltunen Teemu; 26.01.2023
 */

/**
 * Ohjelman ideana on kysyä erilaisia toimintoja siilelle kuten laittaa siili puhumaan, juoksemaan tai luoda uusi siili.
 * Ideana on harjaantua luokkien, metodien ja asettajien (setters) ja noutajien (getters) kanssa sekä luoda toimivaa koodia.
 *
*/



package main;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        Hedgehog hedgehog = new Hedgehog();

        Scanner input = new Scanner(System.in);

        boolean exit = false;
        while (!exit) {

            System.out.println("1) Pistä siili puhumaan, 2) Luo uusi siili, 3) Juoksuta siiliä, 0) Lopeta ohjelma");

            if (input.hasNext()) {
                int i = 0;
                String stringInput = input.nextLine();
                i = Integer.parseInt(stringInput);

                switch (i) {
                    case 1:

                        System.out.println("Mitä siili sanoo:");
                        String sentence = input.nextLine();
                        if (sentence.isEmpty()) {
                            hedgehog.speak("");
                        } else {
                            hedgehog.speak(sentence);
                        }
                        break;

                    case 2:

                        System.out.println("Anna siilin nimi:");
                        String name = input.nextLine();
                        hedgehog.setName(name);

                        System.out.println("Anna siilin ikä:");
                        int age = Integer.parseInt(input.nextLine());
                        hedgehog.setAge(age);
                        break;

                    case 3:

                        System.out.println("Kuinka monta kierrosta?");
                        int rounds = Integer.parseInt(input.nextLine());
                        hedgehog.run(rounds);
                        break;

                    case 0:

                        System.out.println("Kiitos ohjelman käytöstä.");
                        exit = true;
                        break;

                    default:
                        System.out.println("Syöte oli väärä");
                        break;
                }
            }
        }
        input.close();
    }

}



// Tiedoston loppu
