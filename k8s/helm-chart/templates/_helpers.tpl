{{/* =========================================================================
   _helpers.tpl for prima-app Helm Chart
   ========================================================================= */}}

{{- /*
Generate the full name of the chart release
*/ -}}
{{- define "prima-app.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- /*
Generate a name for the Service Account
*/ -}}
{{- define "prima-app.serviceAccountName" -}}
{{- $sa := .Values.serviceAccount | default (dict "create" true "name" "") -}}
{{- if $sa.create -}}
{{- default (include "prima-app.fullname" .) $sa.name -}}
{{- else -}}
{{- $sa.name -}}
{{- end -}}
{{- end -}}

{{- /*
Generate labels for all resources
*/ -}}
{{- define "prima-app.labels" -}}
app.kubernetes.io/name: {{ include "prima-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{- /*
Generate a short name
*/ -}}
{{- define "prima-app.name" -}}
{{- .Chart.Name -}}
{{- end -}}

{{- /*
Generate selector labels for Deployments / Services
*/ -}}
{{- define "prima-app.selectorLabels" -}}
app.kubernetes.io/name: {{ include "prima-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{- /*
Generate container image string
*/ -}}
{{- define "prima-app.image" -}}
{{- printf "%s:%s" .Values.image.repository .Values.image.tag -}}
{{- end -}}

{{- /*
Generate common annotations
*/ -}}
{{- define "prima-app.annotations" -}}
{{- if .Values.annotations }}
{{- toYaml .Values.annotations | nindent 4 }}
{{- end }}
{{- end -}}

