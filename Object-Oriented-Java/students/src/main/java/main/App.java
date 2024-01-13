package main;

import java.util.Scanner;



public class App {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int choice = 0;
        String stringInput;


        System.out.println("Tervetuloa Gifu-järjestelmään");
        System.out.println("Mille yliopistolle haluat ottaa järjestelmän käyttöön?");
        String universityName = input.nextLine();
        Gifu gifu = new Gifu(universityName);
    
        Boolean exit = false;
        while(exit != true) {

            // Menu:
            System.out.print("1) Luo uusi kurssi, 2) Luo uusi opiskelija, ");
            System.out.print("3) Listaa kurssit, 4) Listaa opiskelijat, ");
            System.out.print("5) Lisää opiskelija kurssille, 6) Anna kurssiarvosanat, ");
            System.out.println("0) Lopeta ohjelma");

            if(input.hasNext()) {
                // Choice input from user:
                stringInput = input.nextLine();
                choice = Integer.parseInt(stringInput);

                switch (choice) {
                    case 1:
                        System.out.println("Anna kurssin nimi:");
                        String courseName = input.nextLine();
                        System.out.println("Anna kurssin ID:");
                        String courseID = input.nextLine();
                        System.out.println("Anna kurssin maksimi opiskelijamäärä:");
                        int maxStudentCount = Integer.parseInt(input.nextLine());

                        Course course = new Course(courseName, courseID, maxStudentCount);
                        
                        gifu.addCourse(course);
                        break;

                    case 2:
                        System.out.println("Anna opiskelijan nimi:");
                        String studentName = input.nextLine();
                        System.out.println("Anna opiskelijan opiskelijanumero:");
                        String studentID = input.nextLine();

                        Student student = new Student(studentName, studentID);

                        gifu.addStudent(student);
                        break;

                    case 3:
                        gifu.listCourses();
                        break;

                    case 4:
                        gifu.listStudents();
                        break;

                    case 5:
                        gifu.listCourses();
                        System.out.println("Mille kurssille haluat lisätä opiskelijan? Syötä kurssin numero:");
                        int courseChoice = Integer.parseInt(input.nextLine());

                        gifu.listStudents();
                        System.out.println("Minkä opiskelijan haluat lisätä kurssille? Syötä opiskelijan numero:");
                        int studentChoice = Integer.parseInt(input.nextLine());

                        Student newStudent = gifu.getStudent(courseChoice);
                        Course newCourse = gifu.getCourse(studentChoice);

                        gifu.enrollStudent(newStudent, newCourse);
                        break;
                    
                    case 6:
                        gifu.listCourses();
                        System.out.println("Minkä kurssin haluat arvostella? Syötä kurssin numero:");
                        int gradeCourse = Integer.parseInt(input.nextLine());

                        Course courseForGrading = gifu.getCourse(gradeCourse);
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
