import React, {useState} from 'react';
import classes from './Calculator.module.css';

function Calculator(){
    function handleClick()
    {

    }

    return(
        <div className = {classes.container}>
            <form>
                <input type = "text " value = "0"></input>
            </form>
                <div className = {classes.keypad}>
                <button onClick ={handleClick}>0</button>
                <button onClick ={handleClick}>1</button>
                <button onClick ={handleClick}>2</button>
                <button onClick ={handleClick}>3</button>
                <button onClick ={handleClick}>4</button>
                <button onClick ={handleClick}>5</button>
                <button onClick ={handleClick}>6</button>
                <button onClick ={handleClick}>7</button>
                <button onClick ={handleClick}>8</button>
                <button onClick ={handleClick}>9</button>
                <button onClick ={handleClick}>+</button>
                <button onClick ={handleClick}>-</button>
                <button onClick ={handleClick}>/</button>
                <button onClick ={handleClick}>*</button>
                <button onClick ={handleClick}>^</button>
                <button onClick ={handleClick}>Clear</button>

            </div>
        </div>

);
}

export default Calculator;