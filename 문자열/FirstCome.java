package com.example;

import java.util.Scanner;

public class Main {

    private String solution(String input) {
        
        String result = "";

        for(int i = 0; i < input.length(); i++){
            if (i == input.indexOf(input.charAt(i))){
                System.out.print(input.charAt(i));
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        System.out.println(T.solution(input));

        sc.close();
    }

    
}