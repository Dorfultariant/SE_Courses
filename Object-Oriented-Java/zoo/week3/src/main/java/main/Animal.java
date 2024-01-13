package main;

public class Animal {
    private String species, name;
    private int age;


    // Basic animal:
    public Animal() {
        this("Härkä","Heikki",40);
    }

    // Custom animal:
    public Animal(String species, String name, int age) {
        this.species = species;
        this.name = name;
        this.age = age;
    }


    // Species setnget
    public void setSpecies(String species) {
        this.species = species;
    }
    public String getSpecies() {
        return species;
    }


    // Name setnget
    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }

    // Age setnget
    public void setAge(int age) {
        this.age = age;
    }
    public int getAge() {
        return age;
    }

    


}
