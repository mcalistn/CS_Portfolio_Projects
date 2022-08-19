import * as exercises from './exercises_model.mjs';
import express from 'express';

const PORT = 3000;

const app = express();

app.use(express.json());


/**
 * Create a new exercise with the name, reps, weight, unit and date provided in the body of the POST
 */
 app.post('/exercises', (req, res) => {
    exercises.createExercise(req.body.name, req.body.reps, req.body.weight, 
                             req.body.unit, req.body.date)
        .then(exercise => {
            res.status(201).json(exercise);
        })
        .catch(error => {
            console.error(error);
            // In case of an error, send back status code 400 in case of an error.
            res.status(400).json({ Error: 'Request failed' });
        });
});


/**
 * Find an exercise by passing the ID as a parameter in the URL (not a query value)
 */
app.get('/exercises/:id', (req, res) => {
    const exerciseId = req.params.id;
    exercises.findExerciseById(exerciseId)
        .then(exercise => { 
            if (exercise !== null) {
                res.json(exercise);
            } else {
                res.status(404).json({ Error: 'Resource not found' });
            }         
         })
        .catch(error => {
            res.status(400).json({ Error: 'Request failed' });
        });

});


/**
 * Find all exercises currently in the database
 */
app.get('/exercises', (req, res) => {
    let filter = {};
    exercises.findExercises(filter, '', 0)
        .then(exercises => {
            res.send(exercises);
        })
        .catch(error => {
            console.error(error);
            res.send({ Error: 'Request failed' });
        });

});


/**
 * Edit an exercise's name, reps, weight, unit and/or date
 */
app.put('/exercises/:_id', (req, res) => {
    exercises.replaceExercise(req.params._id, req.body.name, 
                                              req.body.reps, 
                                              req.body.weight, 
                                              req.body.unit, 
                                              req.body.date)
        .then(numUpdated => {
            if (numUpdated === 1) {
                res.json({ _id: req.params._id, name: req.body.name,
                                                reps: req.body.reps,
                                                weight: req.body.weight,
                                                unit: req.body.unit,
                                                date: req.body.date })
            } else {
                res.status(404).json({ Error: 'Resource not found' });
            }
        })
        .catch(error => {
            console.error(error);
            res.status(400).json({ Error: 'Request failed' });
        });
});


/**
 * Find an exercise by passing the ID as a parameter in the URL (not a query value)
 */
app.delete('/exercises/:id', (req, res) => {
    exercises.deleteById(req.params.id)
        .then(deletedCount => {
            if (deletedCount === 1) {
                res.status(204).send();
            } else {
                res.status(404).json({ Error: 'Resource not found' });
            }
        })
        .catch(error => {
            console.error(error);
            res.send({ error: 'Request failed' });
        });
});


// Listening on port 3000...
app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}...`);
});