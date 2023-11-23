<script setup>
import { computed, defineProps, ref } from "vue";
import { useMapStore } from "../../store/mapStore";

const props = defineProps([
	"chart_config",
	"activeChart",
	"series",
	"map_config",
]);
const mapStore = useMapStore();

const chartOptions = ref({
	tooltip: {
		theme: "dark", // 使用浅色主题，或者 'dark' 用于深色主题
		style: {
			fontSize: "12px",
			fontFamily: "Helvetica, Arial, sans-serif",
			colors: ["#000000"], // 设置工具提示文字为黑色
		},
		x: {
			show: true,
			format: "dd MMM",
			formatter: undefined,
		},
	},
	colors: props.chart_config.color,
	grid: {
		show: false,
	},
	legend: {
		show: false,
	},
	stroke: {
		width: [0, 4],
	},
	labels: ["25以下", "25~29", "30~39", "40~49", "50~64", "65以上"],
	xaxis: {
		title: {
			text: "年齡",
		},
	},
	yaxis: [
		{
			title: {
				text: "萬元",
			},
		},
	],
	chart: {
		height: 350,
		type: "line",
		toolbar: {
			show: false,
		},
	},
});
</script>

<template>
	<div id="chart">
		<apexchart
			type="line"
			height="350"
			:options="chartOptions"
			:series="series"
		></apexchart>
	</div>
</template>
