import React from 'react'
import {NavigationContainer} from '@react-navigation/native'
import StackNav from './src/navigation/StackNav'

export default function App(WrappedComponent) {
    return (
        <NavigationContainer>
            <StackNav />
        </NavigationContainer>
    );
}