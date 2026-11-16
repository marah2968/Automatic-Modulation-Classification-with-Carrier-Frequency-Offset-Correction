#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.6.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import iio
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import gnuradioRecieve_epy_block_1_0 as epy_block_1_0  # embedded python block
import math
import sip



class gnuradioRecieve(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "gnuradioRecieve")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.samp_rate = samp_rate = 200e3
        self.nfilts = nfilts = 32
        self.alpha = alpha = 0.35
        self.tx_attenuation = tx_attenuation = 10
        self.rx_gain_0 = rx_gain_0 = 20
        self.rx_gain = rx_gain = 20
        self.rcc_taps = rcc_taps = firdes.root_raised_cosine(1, 1*samp_rate,samp_rate/sps, alpha, nfilts)
        self.constellation = constellation = digital.constellation_8psk().base()
        self.center_freq = center_freq = 915e6

        ##################################################
        # Blocks
        ##################################################

        self._tx_attenuation_range = Range(0, 89, 1, 10, 200)
        self._tx_attenuation_win = RangeWidget(self._tx_attenuation_range, self.set_tx_attenuation, "'tx_attenuation'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._tx_attenuation_win)
        self._rx_gain_0_range = Range(0, 89, 1, 20, 200)
        self._rx_gain_0_win = RangeWidget(self._rx_gain_0_range, self.set_rx_gain_0, "'rx_gain_0'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._rx_gain_0_win)
        self._rx_gain_range = Range(0, 89, 1, 20, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, "'rx_gain'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._rx_gain_win)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1 = qtgui.time_sink_f(
            100, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_y_axis(-.2, constellation.arity()-1+0.2)

        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.enable_stem_plot(False)


        labels = ['Constellation Receiver Decoded', 'Costas Im', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_0_1_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_0_1_0_1_win)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0 = qtgui.time_sink_f(
            (1024*8), #size
            samp_rate, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_y_axis(sps*0.99, sps*1.01)

        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.enable_stem_plot(False)


        labels = ['Sync T_inst', 'Sync T_avg', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0_win)
        self.qtgui_histogram_sink_x_0_0 = qtgui.histogram_sink_f(
            100000,
            100,
            (-1),
            1,
            "",
            1,
            None # parent
        )

        self.qtgui_histogram_sink_x_0_0.set_update_time(0.10)
        self.qtgui_histogram_sink_x_0_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0_0.enable_accumulate(False)
        self.qtgui_histogram_sink_x_0_0.enable_grid(False)
        self.qtgui_histogram_sink_x_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers= [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_0_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_histogram_sink_x_0_0_win)
        self.qtgui_const_sink_x_1_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0.enable_grid(False)
        self.qtgui_const_sink_x_1_0.enable_axis_labels(True)


        labels = ['Sync', 'Costas', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_0_win)
        self.iio_pluto_source_0_0 = iio.fmcomms2_source_fc32('' if '' else iio.get_pluto_uri(), [True, True], 32768)
        self.iio_pluto_source_0_0.set_len_tag_key('packet_len')
        self.iio_pluto_source_0_0.set_frequency(915000000)
        self.iio_pluto_source_0_0.set_samplerate(int(samp_rate))
        self.iio_pluto_source_0_0.set_gain_mode(0, 'manual')
        self.iio_pluto_source_0_0.set_gain(0, 10)
        self.iio_pluto_source_0_0.set_quadrature(True)
        self.iio_pluto_source_0_0.set_rfdc(True)
        self.iio_pluto_source_0_0.set_bbdc(True)
        self.iio_pluto_source_0_0.set_filter_params('Auto', '', 0, 0)
        self.epy_block_1_0 = epy_block_1_0.blk(example_param=1)
        self.digital_symbol_sync_xx_0_0 = digital.symbol_sync_cc(
            digital.TED_SIGNAL_TIMES_SLOPE_ML,
            sps,
            0.045,
            1.0,
            1.0,
            .1,
            8,
            constellation,
            digital.IR_PFB_MF,
            nfilts,
            rcc_taps)
        self.digital_fll_band_edge_cc_0_0 = digital.fll_band_edge_cc(sps, alpha, 17, (2*math.pi/sps/100/sps))
        self.digital_diff_decoder_bb_0_0 = digital.diff_decoder_bb(constellation.arity(), digital.DIFF_DIFFERENTIAL)
        self.digital_constellation_receiver_cb_0_0 = digital.constellation_receiver_cb(constellation, (2*math.pi/100), (-math.pi), math.pi)
        self.blocks_throttle2_0_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_gr_complex*1, int(samp_rate))
        self.blocks_null_sink_0_2 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_1_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.analog_agc_xx_0_0 = analog.agc_cc((1e-4), 1.0, 10)
        self.analog_agc_xx_0_0.set_max_gain(65536)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0_0, 0), (self.digital_fll_band_edge_cc_0_0, 0))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1, 0))
        self.connect((self.blocks_skiphead_0_0, 0), (self.digital_symbol_sync_xx_0_0, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.epy_block_1_0, 0))
        self.connect((self.digital_constellation_receiver_cb_0_0, 1), (self.blocks_null_sink_0_0_0_0, 0))
        self.connect((self.digital_constellation_receiver_cb_0_0, 2), (self.blocks_null_sink_0_0_1, 0))
        self.connect((self.digital_constellation_receiver_cb_0_0, 3), (self.blocks_null_sink_0_2, 0))
        self.connect((self.digital_constellation_receiver_cb_0_0, 0), (self.digital_diff_decoder_bb_0_0, 0))
        self.connect((self.digital_constellation_receiver_cb_0_0, 4), (self.qtgui_const_sink_x_1_0, 1))
        self.connect((self.digital_diff_decoder_bb_0_0, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0_0, 0), (self.blocks_skiphead_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0, 1), (self.blocks_null_sink_0_1_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0, 0), (self.blocks_throttle2_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0, 0), (self.digital_constellation_receiver_cb_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0, 0), (self.qtgui_const_sink_x_1_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0, 3), (self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0, 1))
        self.connect((self.digital_symbol_sync_xx_0_0, 2), (self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0, 0))
        self.connect((self.epy_block_1_0, 0), (self.qtgui_histogram_sink_x_0_0, 0))
        self.connect((self.iio_pluto_source_0_0, 0), (self.analog_agc_xx_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "gnuradioRecieve")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rcc_taps(firdes.root_raised_cosine(1, 1*self.samp_rate, self.samp_rate/self.sps, self.alpha, self.nfilts))
        self.digital_fll_band_edge_cc_0_0.set_loop_bandwidth((2*math.pi/self.sps/100/self.sps))
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_y_axis(self.sps*0.99, self.sps*1.01)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_rcc_taps(firdes.root_raised_cosine(1, 1*self.samp_rate, self.samp_rate/self.sps, self.alpha, self.nfilts))
        self.blocks_throttle2_0_0.set_sample_rate(self.samp_rate)
        self.iio_pluto_source_0_0.set_samplerate(int(self.samp_rate))
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_0_0_0_1_0_1.set_samp_rate(self.samp_rate)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rcc_taps(firdes.root_raised_cosine(1, 1*self.samp_rate, self.samp_rate/self.sps, self.alpha, self.nfilts))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.set_rcc_taps(firdes.root_raised_cosine(1, 1*self.samp_rate, self.samp_rate/self.sps, self.alpha, self.nfilts))

    def get_tx_attenuation(self):
        return self.tx_attenuation

    def set_tx_attenuation(self, tx_attenuation):
        self.tx_attenuation = tx_attenuation

    def get_rx_gain_0(self):
        return self.rx_gain_0

    def set_rx_gain_0(self, rx_gain_0):
        self.rx_gain_0 = rx_gain_0

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain

    def get_rcc_taps(self):
        return self.rcc_taps

    def set_rcc_taps(self, rcc_taps):
        self.rcc_taps = rcc_taps

    def get_constellation(self):
        return self.constellation

    def set_constellation(self, constellation):
        self.constellation = constellation

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq




def main(top_block_cls=gnuradioRecieve, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
