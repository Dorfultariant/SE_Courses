package main;


import java.util.ArrayList;

public class Zoo {
    private String zooName;
    private ArrayList<Animal> animals = new ArrayList<Animal>();

    // If we wanted to be able to create basic zoo
    // public Zoo() {
    //     this("Korkeasaari");
    // }
    
    // Zoo with custom name:
    public Zoo(String zooName) {
        this.zooName = zooName;
    }

    // If we wanted to at some point change the name of the Zoo:
    // public void setZooName(String zooName) {
    //     this.zooName = zooName;
    // }

    public void addAnimal(Animal ob) {
        animals.add(ob);
    }

    // It's beautiful:
    public void listAnimals() {
        System.out.println(zooName + " pitää sisällään seuraavat eläimet:");
        for (int i = 0; i < animals.size(); i++) {
            System.out.println(animals.get(i).getSpecies() + ": " +
                                animals.get(i).getName() + ", " +
                                animals.get(i).getAge() + " vuotta"
                                );
        }
    }
    // So is this one ->
    public void runAnimals(int rounds) {
        for (int i = 0; i < animals.size(); i++) {
            for (int j = 0; j < rounds; j++) {
                System.out.println(animals.get(i).getName() + " juoksee kovaa vauhtia!");
            }
        }
    }
}
