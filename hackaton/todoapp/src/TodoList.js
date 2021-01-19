import React, { Component } from "react";
import TodoItems from "./TodoItems";
import "./TodoList.css";
import SayHello from "./SayHello";

 
class TodoList extends Component {
    constructor(props) {
        super(props);

        this.state = {
            items: []
          };
          
          
        this.addItem = this.addItem.bind(this);
        this.deleteItem = this.deleteItem.bind(this);
      }
      

      addItem(e) {
          if (this._inputElement.value !== "" && this._inputElementTwo.value !== "" && this._inputElementThree.value !=="")
          {
              var newItem = {
                  text: this._inputElement.value,
                  textTwo: this._inputElementTwo.value,
                  textThree: this._inputElementThree.value,
                  key: Math.random()
              };
              this.setState((prevState) => {

                return {
                    items: prevState.items.concat(newItem)
                }
              });
          }
          else {
            
          }
          this._inputElement.value = "";
          this._inputElementTwo.value = "";
          this._inputElementThree.value = "";
          console.log(this.state.items);

          e.preventDefault();
        }

          deleteItem(key) {
            var filteredItems = this.state.items.filter(function (item) {
              return (item.key !== key);
            });
           
            this.setState({
              items: filteredItems
            });
          }




    
  render() {
    return (
      <div className="todoListMain">
        <div className="header">

            <form onSubmit={this.addItem}>
            <input ref={(a) => this._inputElement = a}
                placeholder="Enter your task...">
            </input>
            <input ref={(b) => this._inputElementTwo = b} 
              placeholder="Task assigned to..."></input>
            <select ref={(c) => this._inputElementThree = c} className="dropdw">
            <option value="" disabled selected>Your Priority</option>
              <option value="High">High Priority</option>
              <option value="Low">Low Priority</option>
            </select>
            <button type="submit">+</button>
          </form>
          <button onClick={SayHello}type="Search">Search</button>
        </div>
        <TodoItems entries={this.state.items}
                    delete={this.deleteItem}/>
      </div>
    );
  }
}
 
export default TodoList;