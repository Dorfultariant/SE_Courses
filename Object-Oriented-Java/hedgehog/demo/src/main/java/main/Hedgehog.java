/**
 * Hiltunen Teemu; 26.01.2023
 */


package main;

public class Hedgehog {

    private String name;
    private int age;

    // Perussiili
    public Hedgehog() {
        name = "Pikseli";
        age = 5;
    }

    // Noutajat ja asettajat:
    public String getName() {
        return this.name;
    }
    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return this.age;
    }
    public void setAge(int age) {
        this.age = age;
    }


    // Custom siili
    public Hedgehog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Siili puhuu -metodi
    public void speak(String sentence) {
        if (sentence.isEmpty()) {
            System.out.println("Olen " + name + " ja ikäni on " + age + " vuotta, mutta antaisitko silti syötteen?");
        } else {
            System.out.println(name + ": " + sentence);
        }
    }

    
    // Siili juoksee -metodi
    public void run(int rounds) {
        for (int i = 0; i < rounds; i++) {
            System.out.println(name + " juoksee kovaa vauhtia!");
        }
    }
}


// Tiedoston loppu
