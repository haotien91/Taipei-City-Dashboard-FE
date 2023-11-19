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
	chart: {
		type: "PolarAreaChart",
		offsetY: 10,
	},
	yaxis: {
		labels: {
			offsetX: 200000,
		},
	},

	colors: props.chart_config.color,
	labels: props.chart_config.categories,
	legend: {
		show: true,
		offsetX: -10,
		position: "top",
		fontSize: "10px",
	},

	stroke: {
		colors: ["#fff"],
	},
	fill: {
		opacity: 0.8,
	},
	responsive: [
		{
			breakpoint: 150,
			options: {
				chart: {
					width: 150,
					height: 200,
				},
				plotOptions: {
					polarArea: {
						rings: {
							strokeWidth: 1,
							strokeColor: "#e8e8e8",
						},
						spokes: {
							strokeWidth: 1,
							connectorColors: "#e8e8e8",
						},
					},
				},
			},
		},
	],
});

function handleDataSelection(e, chartContext, config) {
	if (!props.chart_config.map_filter) {
		return;
	}
	if (config.dataPointIndex !== selectedIndex.value) {
		mapStore.addLayerFilter(
			`${props.map_config[0].index}-${props.map_config[0].type}`,
			props.chart_config.map_filter[0],
			props.chart_config.map_filter[1][config.dataPointIndex]
		);
		selectedIndex.value = config.dataPointIndex;
	} else {
		mapStore.clearLayerFilter(
			`${props.map_config[0].index}-${props.map_config[0].type}`
		);
		selectedIndex.value = null;
	}
}
</script>

<template>
	<div v-if="activeChart === 'PolarAreaChart'">
		<apexchart
			width="90%"
			height="300px"
			type="polarArea"
			:options="chartOptions"
			:series="[40610, 15094, 12234, 108812, 117842]"
			@dataPointSelection="handleDataSelection"
		></apexchart>
	</div>
</template>
