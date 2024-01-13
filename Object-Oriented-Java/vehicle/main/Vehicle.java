package main;



public class Vehicle extends Engine {
    protected String type;
    protected String manufacturer;
    protected String model;
    protected int maxSpeed;
    


    public Vehicle(String type, String manufacturer, String model, int maxSpeed) {
        super(type);
        this.type = type;
        this.manufacturer = manufacturer;
        this.model = model;
        this.maxSpeed = maxSpeed;
    }


    
}
