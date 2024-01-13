package main;

public class Course {
    private int maxStudentCount;
    private String courseName;
    private String id;

    public Course(String coursename, String id, int maxStudentCount) {
        this.courseName = coursename;
        this.id = id;
        this.maxStudentCount = maxStudentCount;
    }

    public String getCourseName() {
        return courseName;
    }

    public String getCourseId() {
        return id;
    }
    
    
    
}
