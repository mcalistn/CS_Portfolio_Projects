import React, { useState } from 'react';
import { useHistory } from "react-router-dom";

export const AddExercisePage = () => {

    const [name, setName] = useState('');
    const [reps, setReps] = useState(0);
    const [weight, setWeight] = useState(0);
    const [unit, setUnit] = useState('kgs');
    const [date, setDate] = useState('');

    const history = useHistory();

    const addExercise = async () => {
        const newExcercise = { name, reps, weight, unit, date };
        const response = await fetch('/exercises', {
            method: 'POST',
            body: JSON.stringify(newExcercise),
            headers: {
                'Content-Type': 'application/json',
            },
        });
        if(response.status === 201){
            alert("Successfully added the exercise!");
        } else {
            alert(`Failed to add exercise, status code = ${response.status}`);
        }
        history.push("/");
    };

    return (
        <div>
            <h1>Add Exercise</h1>
            <input
                type="text"
                placeholder="Enter workout name"
                value={name}
                onChange={e => setName(e.target.value)} />
            <input
                type="number"
                value={reps}
                placeholder="Enter number of reps"
                onChange={e => setReps(e.target.value)} />
            <input
                type="number"
                value={weight}
                placeholder="Enter amount of weight lifted"
                onChange={e => setWeight(e.target.value)} />
            <select 
                type="text"
                value={unit}
                onChange={e => setUnit(e.target.value)}>
                <option value="kgs" selected>kgs</option>
                <option value="lbs">lbs</option>
            </select>
            <input
                type="text"
                placeholder="Enter date (MM/DD/YYYY)"
                value={date}
                onChange={e => setDate(e.target.value)} />                
            <button
                onClick={addExercise}
            >Add</button>
        </div>
    );
}

export default AddExercisePage;