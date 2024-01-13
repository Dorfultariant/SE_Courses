package main;

public class Engine {
    protected String motor;
    protected int power;
    
    public Engine(String type) {
        if(type == "Auto") {
            motor = "V8";
            power = 300;
        } else if(type == "Lentokone") {
            motor = "Suihkumoottori";
            power = 500;
        } else if(type == "Laiva") {
            motor = "Wärtsilä Super";
            power = 1000;
        }
    }

}
