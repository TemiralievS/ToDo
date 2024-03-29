import React from "react"

class ProjectForm extends React.Component{
    constructor(props) {
        super(props)
        this.state = {name: '', user: 0}
    }

    handleChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createProject(this.state.name, this.state.user)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit()}>
                <div>
                    <label for="name">name</label>
                    <input type="text" className="form-control" name="name"
                           value={this.state.name} onChange={(event)=>this.handleChange(event)} />
                </div>
                <div className="form-group">
                    <label for="user">user</label>
                    <input type="number" className="form-control" name="user"
                           value={this.state.user} onChange={(event)=>this.handleChange(event)} />
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}

export default ProjectForm