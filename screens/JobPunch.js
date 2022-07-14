import React, { useState, useEffect, Component } from 'react';
import {
    SafeAreaView,
    ScrollView,
    StatusBar,
    StyleSheet,
    Text,
    TextInput,
    useColorScheme,
    View,
    Colors,
    Button,
    Alert,
    fontcolor,
    TouchableOpacity,
} from 'react-native';

export default class JobPunch extends Component { 
    number = React.useState(null);
    onChangeNumber = React.useState(null);
    render() {
        return (
            <SafeAreaView style={styles.container}>
                <View style={styles.box}>
                    <View style={styles.textbox}>
                        <Text style={styles.title}>
                            Job #:
                        </Text>
                        <TextInput style={styles.input}
                            onChangeText={onChangeNumber}
                            value={number}
                            keyboardType="numeric"
                        />
                    </View>
                    <View style={styles.button}>
                        <TouchableOpacity style={{ width: 150, height: 50, backgroundColor: 'gray', justifyContent: 'center', alignItems: 'center' }} onPress={() => this.props.navigation.navigate("StationPunch")} >
                            <Text style={{ fontSize: 20 }}>Back</Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={{ width: 150, height: 50, backgroundColor: 'gray', justifyContent: 'center', alignItems: 'center' }} onPress={() => this.props.navigation.navigate("UserPunch")} >
                            <Text style={{ fontSize: 20 }}>Enter Job</Text>
                        </TouchableOpacity>
                    </View>
                </View>
            </SafeAreaView>
        );
    }
};


const styles = StyleSheet.create({
    container: {
        justifyContent: 'center',
        backgroundColor: 'black',
        width: '100%',
        height: '100%',
        alignItems: 'center'
    },
    box: {
        flexDirection: 'column',
        backgroundColor: '#001C55',
        alignItems: 'center',
        width: '70%',
        height: '70%',
    },
    title: {
        color: 'white',
        fontSize: 50
    },
    datetitle: {
        color: 'white',
        fontSize: 80
    },
    timetitle: {
        color: 'white',
        fontSize: 100
    },
    date: {
        flex: 2,
        paddingTop: 100,
    },
    time: {
        flex: 2,
    },
    textbox: {
        flex: 1,
        flexDirection: 'row',
        alignItems: 'center'
    },
    input: {
        height: 50,
        width: 100,
        borderWidth: 1,
        marginLeft: 20,
        marginTop: 10,
        textAlign: 'center',
        fontSize: 25,
        justifyContent: 'center', //Centered horizontally
        alignItems: 'center', //Centered vertically

    },
    button: {
        flex: 1,
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center', //Centered vertically

    },
    buttons: {
        width: 150,
        height: 50,
        backgroundColor: 'gray',
        justifyContent: 'center',
        alignItems: 'center',
        fontSize: 25
    }

});
