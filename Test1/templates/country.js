const country = {template :`
<div>

<button type ="button"
class = "btn btn-primary m-2 fload-end"
@click = "addClick">
Add Country
</button>

<table class = "table table-striped">
<thead>
    <tr>
        <th>
            Country Name
        </th>
        <th>
            Population
        </th>
    </tr>
    </thead>
    <tbody>
        <tr v-if = 'checkNew'> 
        <td>
        <input type = "text" v-model = 'cname'/> 
        </td>
        <td>
        <input type = "number" v-model = 'population'/> 
        </td>
        <td>
        <button type="button" @click ="submitClick" 
        class = "btn btn-light mr-1">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-square-fill" viewBox="0 0 16 16">
            <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm10.03 4.97a.75.75 0 0 1 .011 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.75.75 0 0 1 1.08-.022z"/>
            </svg>
        </button>
        </td>
        <td>
        <button type="button" @click ="cancelClick"
        class = "btn btn-light mr-1">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16">
        <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
      </svg>
        </button>
        </td>
        </tr>
        
        <tr v-for = "dt in country">
            <td v-if = "cname != dt.cname">{{dt.cname}}</td>
            <td v-if = "cname != dt.cname">{{dt.population}}</td>
            <td v-if = "cname == dt.cname">
                <input type = "text" v-model = 'cname'/> 
            </td>
            <td v-if = "cname == dt.cname">
                <input type = "number" v-model = 'population'/> 
            </td>
            <td v-if = "cname != dt.cname">
            <button type="button" @click ="editClick(dt)"
            class = "btn btn-light mr-1">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                </svg>
            </button>
        </td>
        <td v-if = "cname != dt.cname">
            <button type="button" @click = "deleteClick(dt.cname)"
            class = "btn btn-light mr-1">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16">
            <path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5ZM11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H2.506a.58.58 0 0 0-.01 0H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1h-.995a.59.59 0 0 0-.01 0H11Zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5h9.916Zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47ZM8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5Z"/>
        </svg>
            </button>
            </td>
            <td v-if = "cname == dt.cname">
            <button type="button" @click ="updateClick(dt)" 
            class = "btn btn-light mr-1">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-square-fill" viewBox="0 0 16 16">
                <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm10.03 4.97a.75.75 0 0 1 .011 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.75.75 0 0 1 1.08-.022z"/>
                </svg>
            </button>
            </td>
            <td v-if = "cname == dt.cname">
            <button type="button" @click ="cancelClick"
            class = "btn btn-light mr-1">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16">
            <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
          </svg>
            </button>
            </td>
        </tr>
    </tbody>

</table>
</div>
`,


data(){
    return{
        country:[],
        checkNew:false,
        cname:"",
        population:0
    }
},
methods:{
    refreshData(){
        axios.get(variables.API_URL+"country/")
        .then((response)=>{
            this.country = response.data;
            console.log(this.country)
        })
    },
    addClick(){
        this.checkNew = !this.checkNew;
        this.population=0;
        this.cname ="";
        console.log("Hello")
    },
    editClick(id){
        this.population=id.population;
        this.cname =id.cname;
    },
    updateClick(dt){
        console.log(dt)
    
        axios.put(variables.API_URL+"country/" + dt.cname +"/", {
            cname:this.cname,
            population:this.population
        })      
        .then((response)=>{
            this.refreshData();
            alert(response.data);
            console.log(this.country);
            this.checkNew = false;
            this.population = null;
            this.cname = null;

        })
    },
    submitClick(){
        axios.post(variables.API_URL+"country/" , {
        population : this.population,
        cname : this.cname
    })
        .then((response)=>{
            this.refreshData();
            alert(response.data);
            console.log(this.country);
            this.checkNew = false;
            this.population = null;
            this.cname = null;

        })
    },
    cancelClick(){
        this.checkNew = false;
        this.population = null;
        this.cname = null;
    },
    deleteClick(id){
        axios.delete(variables.API_URL+"country/" + id+"/").then(()=>
            {   this.population = null;
                this.cname = null;
                console.log(this.country)
                this.country = this.country.filter(dt => dt.population != id);
            });
    }
},


mounted:function(){
    this.refreshData();
}
}