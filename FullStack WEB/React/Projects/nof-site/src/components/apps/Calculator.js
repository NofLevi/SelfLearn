import React, {useState} from 'react';
import classes from './Calculator.module.css';

function Calculator(){
    const [result, setResult] = useState("");

    function handleClick(e)
    {
        setResult(result.concat(e.target.name));
    }

    function clearResult(){
        console.log("clearresulttest");
        setResult("");
    }

    function calculateFunc(){
        try{
            setResult(eval(result).toString());
        }
        catch{
            window.alert("Illgal Calculation:Operation without a number afterward.");
            console.log("Calculation Error");
        }
        
    }

    return(
        <div className = {classes.container}>

            <h1 className = {classes.title}> Calculator </h1>

            <form className= {classes.inputform}>
                <input type = "text " value = {result}></input>
            </form>


            <div className = {classes.keypad}>
                    <button className = {classes.numberbuttons} name = "7" onClick ={handleClick}>7</button>
                    <button className = {classes.numberbuttons} name = "8" onClick ={handleClick}>8</button>
                    <button className = {classes.numberbuttons} name = "9" onClick ={handleClick}>9</button>
                    <button className = {classes.operationbuttons} name = "+" onClick ={handleClick}>+</button>

                    <button className = {classes.numberbuttons} name = "4" onClick ={handleClick}>4</button>
                    <button className = {classes.numberbuttons} name = "5" onClick ={handleClick}>5</button>
                    <button className = {classes.numberbuttons} name = "6" onClick ={handleClick}>6</button>
                    <button className = {classes.operationbuttons} name = "-" onClick ={handleClick}>-</button>

                    <button className = {classes.numberbuttons} name = "1" onClick ={handleClick}>1</button>
                    <button className = {classes.numberbuttons} name = "2" onClick ={handleClick}>2</button>
                    <button className = {classes.numberbuttons} name = "3" onClick ={handleClick}>3</button>
                    <button className = {classes.operationbuttons} name = "/" onClick ={handleClick}>/</button>

                    <button className = {classes.numberbuttons} name = "0"onClick ={handleClick}>0</button>
                    <button className = {classes.operationbuttons} name = "Calculate" onClick ={calculateFunc}>Calculate</button>
                    
                    <button className = {classes.operationbuttons} name = "Clear" onClick ={clearResult}>Clear</button>
                    <button className = {classes.operationbuttons} name = "*" onClick ={handleClick}>*</button>
            </div>
        </div>
);
}

export default Calculator;