<script setup>
import MaterialSymbolsAdd from '~icons/material-symbols/add';
import axios from 'axios'
import TodoModal from '@/components/todoModals.vue'
import MaterialSymbolsEdit from '~icons/material-symbols/edit';
import MaterialSymbolsDelete from '~icons/material-symbols/delete';
import moment from 'moment'
import {ref} from 'vue'
</script>

<template>
    <div class="root">
        <teleport to ="body">
            <div class="modal" v-if="isOpen">
                <TodoModal 
                    @close="isOpen=false,reload()"
                    :mode="modalMode"
                    :dataID="id"
                />
            </div>
        </teleport>
        <div class="table_container" v-if="todo.length > 0">
            <table>
                <thead>
                    <tr>
                        <th>
                            Status
                        </th>
                        <th>
                            Name
                        </th>
                        <th>
                            Description
                        </th>
                        <th>
                            Priority
                        </th>
                        <th>
                            Deadline
                        </th>
                        <th>
                            Action
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="data in todo" :style="{background:rowStatus(data.status)}">
                        <th>
                            <input type="checkbox" class="checkbox" :checked="data.status" @change="changeStatus(data.id, data.status)">
                        </th>
                        <th>
                            {{data.name}}
                        </th>
                        <th>
                            {{data.desc}}
                        </th>
                        <th class="prio_container">
                            <div class="priority" :style="{background:convertColor(data.priority)}">
                                {{data.priority}}
                            </div>
                            
                        </th>
                        <th>
                            {{convertDate(data.deadline)}}
                        </th>
                        <th>
                            <div class="modifier">
                                <material-symbols-edit @click="isOpen=true,modalMode=1,id=data.id, callOpen()" class="modifier_button"/>
                                <material-symbols-delete class="modifier_button" v-on:click="deleteData(data.id)" />
                            </div>
                        </th>
                    </tr>
                </tbody>
            </table>
        </div>
        <div v-else>
                    <p style="text-align: center; color: red; font-weight: bold;">No To Do Available!</p>
        </div>
    </div>
    <div id="button">
        <button class="btn" @click="isOpen=true;modalMode=2"><MaterialSymbolsAdd/></button>
    </div>
</template>
<script>
export default {
    data(){
        return{
            todo: [],
            convertedDate: null,
            isOpen: ref(false),
            modalMode: {
                type: Number,
                default: 0,
            },
            id: {
                type: Number,
                default: 0,
            },
        }
    }, methods: {
        convertDate(value){
            const date = moment(value);
            return(date.format('MMMM D, YYYY'));
        },
        async loadToDoData() {
            const response = await axios.get("http://127.0.0.1:8000/api/todo/");
            this.todo = response.data;
        },
        async deleteData(todo_id){
            const response = await axios.delete("http://127.0.0.1:8000/api/todo/", {data:{id:todo_id}})
            .then(function (response){
                console.log(response.data.message);
                location.reload()
            })
            .catch(function (err){
                console.log(err)
            })
        },
        reload(){
            location.reload();
        },
        convertColor(value){
            if(value == "high"){
                return("red");
            } else if(value == "medium"){
                return("yellow");
            } else {
                return("green");
            }
        },
        async changeStatus(id,status){
            const response = await axios.patch("http://127.0.0.1:8000/api/todo/",{
                id: id,
                status: !status
            })
            .then(function(response){
                console.log(response.data)
                location.reload();
            })
            .catch(function(err){
                console.log(err);
            })
        },
        rowStatus(data){
            if(data){
                return("grey")
            } else {
                return("white")
            }
        }
    }, mounted(){
        this.loadToDoData();
    }
}
</script>
