import React, { Component } from 'react'
import {
    Platform,
    Text,
    View,
    TouchableOpacity,
    StyleSheet,
} from 'react-native'

export function StackScreen(){
        return (
            <View style={styles.container}>
                <Text style={styles.infoText}>Hello, World!{'\n'}This is react native windows{'\n'}This is the Stack Screen</Text>
            </View>
        )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    btn: {
        width: '30%',
        borderWidth: 1,
        borderRadius: 4,
        height: 30,
    },
    infoText: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#000',
    },
    btnText: {
        fontSize: 16,
        color: '#000',
    }
})