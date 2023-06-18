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
    number,
    Colors,
    Button,
    Alert,
    fontcolor,
    TouchableOpacity,
} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

export default function StationPunch({ navigation }) {
    const [machineId, setMachineId] = useState('');
    const empId = navigation.getParam('empId');
    const jobId = navigation.getParam('jobId');

    const handleFinish = async () => {
          await axios.post('/api/clock_in_out', {
            emp_id: empId,
            job_id: jobId,
            mach_id: machineId,
          });
    
          // Perform any necessary post-clock-in actions
    
          navigation.navigate('UserPunch'); // Navigate to the home screen or desired destination
      };

        return (
            <SafeAreaView style={styles.container}>
                <View style={styles.box}>
                    <View style={styles.textbox}>
                        <Text style={styles.title}>
                            Job #:
                        </Text>
                        <TextInput style={styles.input}
                            value={machineId}
                            onChangeText={setMachineId}
                            keyboardType="numeric"
                        />
                    </View>
                    <View style={styles.button}>
                        <TouchableOpacity style={{ width: 150, height: 50, backgroundColor: 'gray', justifyContent: 'center', alignItems: 'center' }} onPress={() => navigation.navigate("UserPunch")} >
                            <Text style={{ fontSize: 20 }}>Back</Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={{ width: 150, height: 50, backgroundColor: 'gray', justifyContent: 'center', alignItems: 'center' }} onPress={() => navigation.navigate("UserPunch")} >
                            <Text style={{ fontSize: 20 }}>Enter Job</Text>
                        </TouchableOpacity>
                    </View>
                </View>
            </SafeAreaView>
        );   
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
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
