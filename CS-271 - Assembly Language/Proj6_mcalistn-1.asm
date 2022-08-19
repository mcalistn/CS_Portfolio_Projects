TITLE Program Proj6_mcalistn     (Proj6_mcalistn.asm)

; Author: Nathan McAlister
; Last Modified: 12/3/2021
; OSU email address: mcalistn@oregonstate.edu
; Course number/section:   CS271 Section 400
; Project Number: Proj6_mcalistn          Due Date: 12/5/2021
; Description:	Program request ten valid integers from the user as an ascii string, 
;				converts that ascii string to a numeric value, stores the numeric,
;				values in an array, converts the numeric values back to ascii 
;				character values, and prints the characters that were entered to
;				the console. The program also displays the sum and truncated average
;				of the user inputted numbers. The modularize procedures are:
;					introduction	-	Procedure introduces the user to the program and requests
;										that the user input ten positive or negative numbers that 
;										will fit into a 32-bit register.
;					ReadVal			-	Gets one positive or negative number from the user, verifies
;										that the number will fit into a 32-bit register and contains
;										no non-numeric characters, converts the string of ascii 
;										digits into is numerical representation, and stores that
;										value in memeory.
;					WriteVal		-	Converts a numeric value into a string of ascii digits, and
;										prints that ascii string to the console.
;					arraySum		-	Calculates the sum of the user inputted numbers.
;					arrayAverage	-	Calculates the truncated average of the user inputted 
;										numbers.
;					farewell		-	Says goodbye to the user.


INCLUDE Irvine32.inc


; MACROS
	; **************************************************************************
	; Name: mGetString
	; Description:	Display a prompt, get the user’s input value, store into 
	;				memory.
	; Preconditions:	None.
	; Postconditions:	ECX, EDX is changed.
	; Receives:			prompt, 
	;					buffer - memory storage location,
	;					bufferLen - memory storage allocated memory length,
	;					byteCount - memory storage location for number of bytes
	;								written to memeory.
	; Returns:			buffer - User input stored in memory location
	;					byteCount - Number of bytes written to buffer
	; **************************************************************************
	mGetString MACRO prompt, buffer, bufferLen, byteCount
		MOV		EDX, prompt
		CALL	WriteString
		MOV		EDX, buffer					; Memory location to store user inputted value
		MOV		ECX, bufferLen
		CALL	ReadString
		MOV		EDI, byteCount
		STOSD
	ENDM


	; **************************************************************************
	; Name: mDisplayString
	; Description:	Print the string which is stored in a specified memory 
	;				location.
	; Preconditions:	Passed string array must be 10 digits long.
	; Postconditions:	EAX, EBX, ECX, EDX, ESI, and EDI are changed.
	; Receives:			strArr - string array containing ascii digits to be
	;							 printed
	;					outNum - value to be translated to ascii digits
	; Returns:			strArry - ascii digits of value
	; **************************************************************************
	mDisplayString MACRO strArr, outNum
		MOV		EAX, 0
		MOV		EBX, 0
		MOV		EDX, 0
		MOV		ESI, outNum
		MOV		EDI, strArr
		LODSD
		CMP		EAX, MAX_NUM				; Checks if passed value is negative
		JBE		_loopNextDigit
		MOV		EBX, EAX
		MOV		EAX, MAX_REG
		SUB		EAX, EBX
		INC		EAX
	_loopNextDigit:							; Converts value to ascii string
		MOV		EBX, 10
		DIV		EBX
		ADD		EDX, 48
		MOV		EBX, EAX
		MOV		EAX, EDX
		CLD
		STOSB								; Stores ascii string in memory
		MOV		EAX, EBX
		MOV		EDX, 0
		CMP		EAX, 0
		JNE		_loopNextDigit
		DEC		EDI
		STD	
		MOV		ESI, strArr					; Writes ascii string to console
		ADD		ESI, 9
		MOV		ECX, 11
		MOV		EDI, outNum
		MOV		EAX, [EDI]
		CMP		EAX, MAX_NUM
		JBE		_nextByte
		MOV		EAX, 2dh					; Adds negative sign to front of printed string
		CALL	WriteChar
		MOV		EAX, 0
	_nextStrArray:
		LODSB
		CMP		EAX, 0
		JE		_nextByte
		CALL	WriteChar
	_nextByte:
		MOV		EAX, 0
		LOOP	_nextStrArray
	ENDM

; CONSTANTS
	MAX_NUM = 2147483647	; Maximum signed integer accepted
	MAX_REG = 4294967295	; Maximum register value


.data

	intro			BYTE	"PROGRAMMING ASSIGNMENT 6: Designing low-level I/O procedures", 13, 10
					BYTE	"Written by: Nathan McAlister", 13, 10, 13, 10
					BYTE	"Please provide 10 signed decimal integers.", 13, 10
					BYTE	"Each number needs to be small enough to fit inside a 32 bit register.", 13, 10
					BYTE	"After you have finished inputting the raw numbers I will display a", 13, 10
					BYTE	"list of the integers, their sum, and their average value.", 13, 10, 13, 10, 0
	prompt1			BYTE	"Please enter an signed number: ", 0
	prompt2			BYTE	"You entered the following numbers: ", 0
	prompt3			BYTE	"The sum of these numbers is: ", 0
	prompt4			BYTE	"The truncated average is: ", 0
	error			BYTE	"ERROR: You did not enter a signed number or your number was too big. ", 0
	goodbye			BYTE	"Thanks for playing!", 13, 10, 13, 10, 0
	strOutput		BYTE	13 DUP(0), 0
	outputString	BYTE	13 DUP(0), 0
	numOutput		SDWORD	0
	strMaxLen		SDWORD	SIZEOF strOutput
	strByteCnt		SDWORD	0
	outputArray		SDWORD	10 DUP(0)
	sum				SDWORD	0
	average			SDWORD	0


.code
main PROC

	; Display introduction message
	PUSHAD
	PUSH	OFFSET intro
	CALL	introduction
	POPAD

	; Get user inputed values
	MOV		ECX, 10						
	MOV		EDI, OFFSET outputArray
_loopReadTen:	
	PUSHAD
	PUSH	OFFSET error
	PUSH	OFFSET numOutput
	PUSH	OFFSET strByteCnt
	PUSH	strMaxLen
	PUSH	OFFSET strOutput
	PUSH	OFFSET prompt1
	CALL	ReadVal
	POPAD
	MOV		EAX, numOutput				; Store values in outputArray
	STOSD									; Store values in outputArray
	MOV		numOutput, 0
	LOOP	_loopReadTen
	CALL	CrLf

	; Display user inputted values
	MOV		EDX, OFFSET prompt2
	CALL	WriteString
	CALL	CrLf
	MOV		ECX, 11						
	MOV		ESI, OFFSET outputArray
_loopWriteTen:	
	PUSHAD
	PUSH	ECX
	PUSH	ESI
	PUSH	OFFSET outputString
	CALL	WriteVal
	POP		ESI
	POP		ECX
	POPAD
	ADD		ESI, TYPE outputArray
	CMP		ECX, 1
	JE		_lastNum
	MOV		EAX, 44						; Write the character ',' (comma)
	CALL	WriteChar
	MOV		EAX, 32						; Write the character ' ' (space)
	CALL	WriteChar
_lastNum:
	LOOP	_loopWriteTen
	CALL	CrLf

	; Calculate sum of inputted numbers
	PUSHAD
	PUSH	OFFSET outputString
	PUSH	OFFSET prompt3
	PUSH	OFFSET sum
	PUSH	OFFSET outputArray
	CALL	arraySum
	POPAD
	
	; Calculate truncated average of inputted numbers
	PUSHAD
	PUSH	OFFSET sum
	PUSH	OFFSET outputString
	PUSH	OFFSET prompt4
	PUSH	OFFSET average
	CALL	arrayAverage
	CALL	CrLf
	CALL	CrLf
	POPAD

	; Display farewell message
	PUSHAD
	PUSH	OFFSET goodbye
	CALL	farewell
	POPAD

	Invoke ExitProcess,0	; exit to operating system
main ENDP


; **************************************************************************
; Name: introduction
; Description:	Procedure introduces the user to the program and requests
;				that the user input ten positive or negative numbers that 
;				will fit into a 32-bit register.
; Preconditions:	None.
; Postconditions:	EDX is changed.
; Receives:			intro (r)
; Returns:			None.
; **************************************************************************
introduction PROC
	PUSH	EBP
	MOV		EBP, ESP
	MOV		EDX, [EBP + 8]
	CALL	WriteString
	POP		EBP
	RET		4
introduction ENDP


; **************************************************************************
; Name: ReadVal
; Description:	Gets one positive or negative number from the user, verifies
;				that the number will fit into a 32-bit register and contains
;				no non-numeric characters, converts the string of ascii 
;				digits into is numerical representation, and stores that
;				value in memeory.
; Preconditions:	None.
; Postconditions:	EAX, EBX, ECX, EDX, ESI, and EDI are changed.
; Receives:			prompt1 (r), strOutput (r), strMaxLen (v), 
;					strByteCnt (r), numOutput (r), error (r)
; Returns:			numOutput
; **************************************************************************
ReadVal PROC
	PUSH	EBP
	MOV		EBP, ESP
_loopAgain:
	PUSHAD
	mGetString	[EBP + 8], [EBP + 12], [EBP + 16], [EBP + 20]
	POPAD
	MOV		ESI, [EBP + 20]
	LODSD
	MOV		ECX, EAX
	CLD
	MOV		EAX, 0
	MOV		ESI, [EBP + 12]
	LODSB
	CMP		ECX, 1
	JBE		_loopNextStr
	MOV		EBX, 2bh
	CMP		EAX, EBX
	JE		_plusMinus
	MOV		EBX, 2dh
	CMP		EAX, EBX
	JE		_plusMinus
	_loopNextStr:
		MOV		EBX, EAX
		CMP		EBX, 48
		JB		_error
		CMP		EBX, 57
		JA		_error
		MOV		EDI, [EBP + 24]
		MOV		EAX, [EDI]
		MOV		EDX, 10
		MUL		EDX
		CMP		EAX, MAX_NUM
		JA		_error		
		SUB		EBX, 48
		ADD		EAX, EBX
		CMP		EAX, MAX_NUM
		JA		_error		
		MOV		EDI, [EBP + 24]
		STOSD							; Returns user input value in numOutput if a positive integer	
		_plusMinus:
		MOV		EAX, 0
		LODSB
		LOOP	_loopNextStr
	JMP		_finishLoop
_error:	
	MOV		EDX, [EBP + 28]
	CALL	WriteString
	CALL	CrLf
	MOV		EDI, [EBP + 24]
	MOV		EAX, 0
	STOSD
	JMP		_loopAgain
_finishLoop:
	MOV		EAX, 0
	MOV		ESI, [EBP + 12]
	LODSB
	MOV		EBX, 2dh					; Returns user input value in numOutput if a negative integer
	CMP		EAX, EBX
	JNE		_positive
	MOV		EDI, [EBP + 24]
	MOV		EAX, [EDI]
	NEG		EAX							; Converts to numOutput to a negative value
	STOSD
_positive:
	POP		EBP
	RET		24
ReadVal ENDP


; **************************************************************************
; Name: WriteVal
; Description:	Converts a numeric value into a string of ascii digits, and
;				prints that ascii string to the console.
; Preconditions:	Value cannot be more than 10 digits long.
; Postconditions:	EAX, BL, EBX, ECX, EDX, ESI, and EDI are changed.
; Receives:			outputString (r), outputArray (r)
; Returns:			outputString (clears)
; **************************************************************************
WriteVal PROC
	PUSH	EBP
	MOV		EBP, ESP
	PUSHAD
	mDisplayString	[EBP + 8], [EBP + 12]
	POPAD
	MOV		ESI, [EBP + 8]					; Returns outputString to all zeroes
	MOV		ECX, 10
_clearArray:
	MOV		BL, 0
	MOV		[ESI], BL
	INC		ESI
	LOOP	_clearArray
	POP		EBP
	RET		4
WriteVal ENDP


; **************************************************************************
; Name: arraySum
; Description:	Calculates the sum of the user inputted numbers.
; Preconditions:	Sum must fit into a 32-bit register.
; Postconditions:	EAX, EBX, BL, ECX, EDX, ESI, and EDI are changed.
; Receives:			outputArray (r), sum (r), prompt3 (r), outputString (r)
; Returns:			sum, outputString (clears)
; **************************************************************************
arraySum PROC
	PUSH	EBP
	MOV		EBP, ESP
	MOV		ESI, [EBP + 8]
	MOV		EDI, [EBP + 12]
	MOV		EAX, 0
	MOV		ECX, 10
_loopSum:
	MOV		EBX, [ESI]						
	ADD		EAX, EBX
	ADD		ESI, TYPE SDWORD
	LOOP	_loopSum
	STOSD									; Returns sum in memeory
	MOV		EDX, [EBP + 16]
	CALL	WriteString
	PUSHAD
	mDisplayString	[EBP + 20], [EBP + 12]
	POPAD
	MOV		ESI, [EBP + 20]					; Returns outputString to all zeroes
	MOV		ECX, 10
_clearArray:
	MOV		BL, 0
	MOV		[ESI], BL
	INC		ESI
	LOOP	_clearArray
	CALL	CrLf
	POP		EBP
	RET		16
arraySum ENDP


; **************************************************************************
; Name: arrayAverage
; Description:	Calculates the truncated average of the user inputted 
;				numbers.
; Preconditions:	Average must fit into a 32-bit register.
; Postconditions:	EAX, EBX, ECX, EDX, ESI, and EDI are changed.
; Receives:			average (r), prompt4 (r), outputString (r), sum (r)
; Returns:			average
; **************************************************************************
arrayAverage PROC
	PUSH	EBP
	MOV		EBP, ESP
	MOV		EDX, [EBP + 12]
	CALL	WriteString
	MOV		EDX, 0
	MOV		ESI, [EBP + 20]
	MOV		EAX, [ESI]
	MOV		EBX, 10
	CDQ
	IDIV	EBX
	MOV		EDI, [EBP + 8]
	STOSD									; Returns average in memory
	PUSHAD
	mDisplayString	[EBP + 16], [EBP + 8]
	POPAD
	POP		EBP
	RET		16
arrayAverage ENDP


; **************************************************************************
; Name: farewell
; Description:	Says goodbye to the user
; Preconditions:	None.
; Postconditions:	EDX is changed.
; Receives:			goodbye
; Returns:			None.
; **************************************************************************
farewell PROC
	PUSH	EBP
	MOV		EBP, ESP
	MOV		EDX, [EBP + 8]
	CALL	WriteString
	POP		EBP
	RET		4
farewell ENDP

END main
