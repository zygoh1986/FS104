import React, { Component } from "react";
import FlipMove from "react-flip-move";
import SayHello from './SayHello'


 
class TodoItems extends Component {
    constructor(props){
        super(props);

        this.createTasks = this.createTasks.bind(this);
    }
  
  
  createTasks(item) {
  return (
    <div className="result">
      <SayHello />
    <li onClick={() => this.delete(item.key)}  
                          key={item.key}>
                            <b>Task:</b> {item.text} 
                            <br></br><b>Assigned to:</b> {item.textTwo} 
                            <br></br><b>Priority:</b> {item.textThree}
                            </li>
    </div>
  )}

  delete(key) {
      this.props.delete(key);
  }
 
  render() {
    
    var todoEntries = this.props.entries;
    todoEntries.sort(function(a, b){
      var itemA = a.textThree;
      var itemB = b.textThree;
      if (itemA < itemB)
      {
        return -1; 
      }
      return 0;
    })
    var listItems = todoEntries.map(this.createTasks);
    
    
    return (
      <ul className="theList">
          <FlipMove duration = {250} easing="ease-out">
          {listItems}
          </FlipMove>
          
      </ul>
    );
  }
};
 
export default TodoItems;