import React, { Component } from 'react'
import { createStackNavigator } from '@react-navigation/stack'
import UserPunch from '../routes/UserPunch'
import JobPunch from '../routes/JobPunch'
import StationPunch from '../routes/StationPunch'

const Stack = createStackNavigator()

export default function StackNav() {
    return (
        <Stack.Navigator initialRouteName="UserPunch">
            <Stack.Screen name='UserPunch' component={UserPunch} />
            <Stack.Screen name='JobPunch' component={JobPunch} />
            <Stack.Screen name='StationPunch' component={StationPunch} />
        </Stack.Navigator>
    );
}
//import React, { Component } from 'react'
//import { createStackNavigator } from '@react-navigation/stack'
//import Home from '../routes/Home'
//import StackScreen from '../routes/StackScreen'

//const Stack = createStackNavigator()

//export default class StackNav extends Component {
//    render() {
//        return (
//            <Stack.Navigator>
//                <Stack.Screen name='Home' component={Home} />
//                <Stack.Screen name='StackScreen' component={StackScreen} />
//            </Stack.Navigator>
//        )
//    }
//}