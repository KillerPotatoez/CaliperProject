import React, { Component } from 'react'
import {
    Platform,
    Text,
    View,
    TouchableOpacity,
    StyleSheet,
    Appearance,
} from 'react-native'

export default class Home extends Component {

    constructor(props) {
        super(props)

        this.state = {
            theme: Appearance.getColorScheme(), // 'dark' or 'light'
        }
    }

    componentDidMount() {
        Appearance.addChangeListener(this.handleThemeChange)
    }

    componentWillUnmount() {
        Appearance.removeChangeListener(this.handleThemeChange)
    }

    handleThemeChange = () => {
        this.setState({
            theme: Appearance.getColorScheme(),
        })
    }

    render() {
        return (
            <View style={[this.state.theme == 'dark' ? styles.dark : styles.light, styles.container]}>
                <Text style={[this.state.theme == 'dark' ? styles.dark : styles.light, styles.infoText]}>Hello, World!{'\n'}This is react native windows</Text>
                <TouchableOpacity style={[this.state.theme == 'dark' ? styles.dark : styles.light, styles.btn]} onPress={() => this.props.navigation.navigate('StackScreen')}>
                    <Text style={[this.state.theme == 'dark' ? styles.dark : styles.light, styles.btnText]}>Stack Screen</Text>
                </TouchableOpacity>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    dark: {
        backgroundColor: '#000',
        color: '#fff',
    },
    light: {
        backgroundColor: '#fff',
        color: '#000',
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
        // color: '#000',
    },
    btnText: {
        fontSize: 16,
        // color: '#000'
    }
})