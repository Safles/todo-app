<script setup>
    import axios from 'axios'
    import {defineEmits} from 'vue'
    import TodoAdd from '@/components/todoAdd.vue';
    import TodoEdit from '@/components/todoEdit.vue'
    import EpBack from '~icons/ep/back';
    defineEmits(["close"])
</script>

<template>
    <div>
        <div v-if="mode==1">
            <TodoEdit
                :id="dataID"
            />
        </div>
        <div v-else-if="mode==2">
            <TodoAdd/>
        </div>
        <div class="modalButton">
            <button class="btn" @click="$emit('close')"><EpBack /></button>
        </div>
    </div>
    
</template>
<script>
export default {
    data (){
        return {
            
        }
    }, methods: {
    },
    name: 'TodoModal',
    props:[
        'mode',
        'dataID',
    ], mounted(){

    }
}

</script>
