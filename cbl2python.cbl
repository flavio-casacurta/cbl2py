       WORKING-STORAGE SECTION.
       01  FILLER  PIC X(30) VALUE 'BEGIN WORKING STORAGE SECTION'.
       01  EXAMPLE-GROUP.
           03      ANOTHER_GROUP OCCURS 0003 TIMES.
            05     FIELD-1                   PIC X(3).
            05     FIELD-2 REDEFINES FIELD-1 PIC 9(3).
            05     FIELD-3 OCCURS 0002 TIMES PIC S9(3)V99.
           03      THIS-IS-ANOTHER-GROUP.
            05     YES                       PIC X(5) VALUE 'NO'.
           03      THIS-IS-ELEMENTARY        PIC 9(5).
       01  FILLER  PIC X(30) VALUE 'END WORKING STORAGE SECTION'.

       PROCEDURE DIVISION.
       MAIN-SECTION SECTION.
       MAIN-L.
           INITIALIZE EXAMPLE-GROUP
           MOVE 5 TO THIS-IS-ELEMENTARY
           MOVE 'YES' TO YES
           IF YES EQUAL TO 'YES'
              GOBACK
           END-IF.
